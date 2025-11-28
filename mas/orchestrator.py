"""
RootAgent Module (formerly Orchestrator)
========================================

This module implements the `RootAgent` for the Multi-Agent System.
It acts as the central coordinator, managing agent tasks, context, and quality.
It follows the "Coordinator" pattern where other agents are treated as tools.
"""

from typing import Any, Dict, List, Optional
from rich.console import Console
from rich.prompt import Prompt
from .memory import LongTermMemory
from .observability import QualityManager
from .context import ContextManager
from agents.base_agent import BaseAgent
from .tool_context import ToolContext
from google_local.adk.plugins import LoggingPlugin

class RootAgent(BaseAgent):
    """
    The RootAgent acts as the central coordinator for the Multi-Agent System.
    It manages the lifecycle of agent tasks, integrates with memory and quality systems,
    and enforces safety gates.
    """

    def __init__(self, memory_system: LongTermMemory, quality_manager: QualityManager, context_manager: ContextManager, auto_approve: bool = False):
        """
        Initialize the RootAgent with essential subsystems.

        Args:
            memory_system (LongTermMemory): The system's long-term memory.
            quality_manager (QualityManager): The system for observability.
            context_manager (ContextManager): The system for context management.
            auto_approve (bool): If True, HITL requests are auto-approved.
        """
        super().__init__(name="RootCoordinator", instruction="Orchestrate the security assessment workflow.")
        self.memory = memory_system
        self.quality = quality_manager
        self.context_manager = context_manager
        self.auto_approve = auto_approve
        self.console = Console()
        
        # Observability Plugin
        self.logging_plugin = LoggingPlugin()
        
        # A2A Communication Bus
        from mas.a2a import Bus
        self.bus = Bus()

    def check_safety(self, action_type: str, details: Dict[str, Any]) -> bool:
        """
        Checks if an action is safe to execute.
        """
        if not self.quality.check_safety_gate(action_type, details):
             self.console.print(f"[bold red]❌ Action Blocked by Safety Policy.[/bold red]")
             return False

        if self.auto_approve:
            return True
            
        response = Prompt.ask("Do you authorize this action?", choices=["y", "n"], default="n")
        return response == "y"

    def run_agent_task(self, agent: Any, task_description: str, *args, **kwargs) -> Dict[str, Any]:
        """
        Execute a task using a specific agent (treated as a tool).
        """
        # Start a trace for this task
        trace_id = self.quality.start_trace(agent.name, task_description)
        self.console.print(f"[bold blue]🚀 Starting Task: {agent.name}[/bold blue]")
        self.console.print(f"Task: {task_description}")
        
        # Notify Logging Plugin
        self.logging_plugin.on_agent_start(agent.name, task_description)

        # 1. Context Engineering
        relevant_memory = self.memory.retrieve_relevant_memory(task_description, limit=5)
        # Extract target_ip from args if present (heuristic)
        target_ip = args[0] if args else kwargs.get('target_ip')
        
        context_payload = {
            "task": task_description,
            "target": target_ip,
            "memory": relevant_memory,
            "history": self.context_manager.get_recent_history(limit=5)
        }
        optimized_context = self.context_manager.optimize_context(context_payload, agent.name)
        self.quality.log_metric(trace_id, "context_size", len(str(optimized_context)))

        # 1.5 Tool Context (HITL)
        # Create a tool context for this execution to handle permission requests
        tool_context = ToolContext(session_id=trace_id, auto_approve=self.auto_approve)

        try:
            # 2. Execution
            if hasattr(agent, 'run'):
                 result = agent.run(optimized_context, tool_context=tool_context)
            elif hasattr(agent, 'scan'):
                 # Fallback for legacy agents with 'scan'
                 # Check if scan accepts tool_context
                 try:
                    result = agent.scan(*args, tool_context=tool_context, **kwargs)
                 except TypeError:
                    result = agent.scan(*args, **kwargs)
            elif hasattr(agent, 'exploit'):
                 # Fallback for legacy agents with 'exploit'
                 try:
                    result = agent.exploit(*args, tool_context=tool_context, **kwargs)
                 except TypeError:
                    result = agent.exploit(*args, **kwargs)
            elif hasattr(agent, task_description) and callable(getattr(agent, task_description)):
                 # Dynamic method call (e.g., for WriterAgent)
                 method = getattr(agent, task_description)
                 result = method(*args, **kwargs)
            elif hasattr(agent, 'generate_report'):
                 result = agent.generate_report(self.memory.get_all_findings())
            else:
                 raise AttributeError(f"Agent {agent.name} has no run/scan/exploit method.")

            # 3. Observability
            # Calculate duration (simulated)
            duration_ms = 100.0 
            self.quality.log_step(
                agent_name=agent.name,
                action="run",
                input_data=task_description,
                output_data=result,
                duration_ms=duration_ms,
                success=True,
                intent=task_description,
                reasoning="Executed via RootAgent"
            )
            
            # Notify Logging Plugin
            self.logging_plugin.on_agent_finish(agent.name, result)
            
            # 4. Memory
            self.memory.store_action(agent.name, task_description, str(result), "COMPLETED", True)
            if isinstance(result, dict) and "findings" in result:
                for finding in result["findings"]:
                    self.memory.store_finding(finding)

            # 5. Quality Check
            quality_score = self.quality.evaluate_step(agent.name, task_description, result)
            self.quality.log_metric(trace_id, "quality_score", quality_score)
            
            self.console.print(f"[bold green]✅ Task Completed (Quality: {quality_score}/10)[/bold green]")
            return result

        except Exception as e:
            self.console.print(f"[bold red]❌ Task Failed: {e}[/bold red]")
            self.quality.log_step(
                agent_name=agent.name,
                action="run",
                input_data=task_description,
                output_data=str(e),
                duration_ms=0.0,
                success=False,
                intent=task_description,
                reasoning="Failed execution"
            )
            self.quality.log_metric(trace_id, "error", str(e))
            
            # Notify Logging Plugin
            self.logging_plugin.on_agent_finish(agent.name, {"error": str(e)})
            
            return {"error": str(e)}
        finally:
            self.quality.end_trace(trace_id)

    def run_refinement_loop(self, draft_agent: Any, critic_agent: Any, method_name: str, report_type: str, *args, **kwargs) -> str:
        """
        Executes a feedback loop between a drafting agent and a critic agent.
        """
        self.console.print(f"\n[bold magenta]🔄 Starting Refinement Loop for {report_type}[/bold magenta]")
        
        # Step 1: Generate Draft
        self.console.print(f"[cyan]Step 1: Generating Draft with {draft_agent.name}...[/cyan]")
        draft_result = self.run_agent_task(draft_agent, method_name, *args, **kwargs)
        
        # Simulation Hack for text content
        draft_text = f"# Draft Report for {report_type}\n\n(Simulated content of {draft_result})"
        
        # Step 2: Critique
        self.console.print(f"[cyan]Step 2: Critiquing Draft with {critic_agent.name}...[/cyan]")
        critique_result = critic_agent.review_report(draft_text, report_type)
        self.console.print(f"[bold yellow]Critique:[/bold yellow]\n{critique_result['critique']}")
        
        # Step 3: Refine
        self.console.print(f"[cyan]Step 3: Finalizing Refined Report...[/cyan]")
        # In a real system, we would pass the critique back to the WriterAgent to rewrite.
        # For this demo, we assume the CriticAgent provides the refined content directly or we save it.
        final_filename = f"refined_{draft_result}"
        self.console.print(f"[bold green]✅ Refinement Complete. Saved to {final_filename}[/bold green]")
        
        return final_filename

    def close(self):
        """Finalizes the session trace."""
        self.quality.end_trace()
