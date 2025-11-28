"""
Observability & Quality Framework Module
========================================

This module implements the "Quality Framework" for the Multi-Agent System.
It is responsible for monitoring, tracing, and evaluating the performance and safety of all agents.

Key Responsibilities:
1.  **Distributed Tracing**: Tracks the execution flow of the entire multi-agent session, assigning a unique `trace_id`.
2.  **Metrics Collection**: Gathers critical operational metrics:
    -   *Latency*: Time taken per step (P99 tracking).
    -   *Token Usage*: Estimated cost and complexity.
    -   *Complexity*: Number of steps to complete a task.
3.  **Safety Gates**: Intercepts actions before execution to prevent dangerous operations (e.g., `rm -rf`, out-of-scope IPs).
4.  **Golden Set Generation**: Automatically saves successful runs as "Golden Sets" for future regression testing.
5.  **Reporting**: Generates detailed efficiency reports (`efficiency_report.md`) at the end of a session.

Design Choices:
-   **Centralized Quality Manager**: A single manager ensures consistent logging and metric aggregation across all agents.
-   **JSON-based Tracing**: Traces are stored as JSON files, making them easy to parse, visualize, and ingest into other tools.
-   **Simulated Metrics**: Token counts are estimated (char/4) to avoid external API dependencies for this demo, but the architecture supports real tokenizers.
"""

import json
import time
import uuid
import os
from typing import Dict, Any, List, Optional
from datetime import datetime
from rich.console import Console

class QualityManager:
    """
    The central observability engine for the MAS.
    
    Attributes:
        log_dir (str): Directory to store trace logs.
        golden_set_dir (str): Directory to store successful "Golden Set" traces.
        current_trace_id (str): The unique ID of the active session.
        THRESHOLDS (Dict): Performance thresholds for the Efficiency Report.
    """
    
    def __init__(self, log_dir: str = "logs", golden_set_dir: str = "golden_sets"):
        self.console = Console()
        self.log_dir = log_dir
        self.golden_set_dir = golden_set_dir
        self.current_trace_id = None
        self.session_traces = [] # Store all traces for session summary
        
        # 1.2 Operational Cost Metrics (Efficiency) Thresholds
        # These thresholds define what constitutes a "passing" grade for the system's performance.
        # They are used in the final Efficiency Report.
        self.THRESHOLDS = {
            "latency_p99_ms": 500.0,       # Max acceptable P99 latency per step (target: fast agents)
            "max_complexity_steps": 15,    # Max steps per agent trajectory (target: concise agents)
            "max_tokens_per_task": 1000    # Max estimated tokens per task (target: cost-effective agents)
        }
        
        # Initialize empty trace data structure
        self.trace_data = {
            "trace_id": "",
            "start_time": "",
            "end_time": "",
            "status": "RUNNING",
            "metrics": {
                "total_duration_ms": 0,
                "tool_calls": 0,
                "errors": 0,
                "total_tokens": 0  # New Metric for cost tracking
            },
            "steps": []
        }
        
        # Ensure directories exist so we don't crash on save
        os.makedirs(self.log_dir, exist_ok=True)
        os.makedirs(self.golden_set_dir, exist_ok=True)

    def start_trace(self, agent_name: str = "System", task_description: str = "Global Session") -> str:
        """
        Starts a new distributed trace for a MAS session.
        
        This should be called at the very beginning of the `main.py` execution.
        It resets the metrics and generates a new UUID.
        
        Args:
            agent_name (str): The name of the agent starting the trace.
            task_description (str): Description of the task.
        
        Returns:
            str: The new trace ID.
        """
        self.current_trace_id = str(uuid.uuid4())
        self.trace_data = {
            "trace_id": self.current_trace_id,
            "root_agent": agent_name,
            "root_task": task_description,
            "start_time": datetime.utcnow().isoformat(),
            "end_time": "",
            "status": "RUNNING",
            "metrics": {
                "total_duration_ms": 0,
                "tool_calls": 0,
                "errors": 0,
                "total_tokens": 0
            },
            "steps": []
        }
        self.console.print(f"[bold blue]ℹ️  Quality Framework: Trace Started ({self.current_trace_id})[/bold blue]")
        return self.current_trace_id

    def end_trace(self, status: str = "COMPLETED"):
        """
        Ends the current trace and saves it to disk.
        
        This method finalizes the metrics (calculating total duration) and writes the
        JSON log file. It also triggers the generation of the Efficiency Report.
        
        Args:
            status (str): The final status of the session ('COMPLETED', 'FAILED').
        """
        self.trace_data["end_time"] = datetime.utcnow().isoformat()
        self.trace_data["status"] = status
        
        # Calculate duration
        start = datetime.fromisoformat(self.trace_data["start_time"])
        end = datetime.fromisoformat(self.trace_data["end_time"])
        duration = (end - start).total_seconds() * 1000
        self.trace_data["metrics"]["total_duration_ms"] = duration

        # Save to Log
        log_file = os.path.join(self.log_dir, f"trace_{self.current_trace_id}.json")
        with open(log_file, "w") as f:
            json.dump(self.trace_data, f, indent=2)
        
        self.console.print(f"[bold blue]ℹ️  Quality Framework: Trace Saved to {log_file}[/bold blue]")
        
        # Add to session traces
        self.session_traces.append(self.trace_data)
        
        # Generate Efficiency Report
        # This creates a human-readable Markdown summary of the run.
        self.generate_efficiency_report()
        
        # Save to Golden Set if successful
        # This implements the "Regression Testing" requirement. If a run was good, keep it.
        if status == "COMPLETED":
            self._save_to_golden_set()

    def _save_to_golden_set(self):
        """
        Saves successful traces as Golden Sets for regression testing.
        """
        golden_file = os.path.join(self.golden_set_dir, f"golden_{self.current_trace_id}.json")
        with open(golden_file, "w") as f:
            json.dump(self.trace_data, f, indent=2)
        self.console.print(f"[bold green]🌟 Quality Framework: Added to Golden Set ({golden_file})[/bold green]")

    def log_step(self, agent_name: str, action: str, input_data: Any, output_data: Any, duration_ms: float, success: bool,
                 intent: str = "", reasoning: str = "", llm_prompt: str = "", llm_response: str = "", state_change: Dict = None):
        """
        Logs a structured step in the agent trajectory with rich context.
        
        This is the core logging function used by the Orchestrator. It captures everything
        needed to reconstruct *why* an agent did something.
        
        Args:
            agent_name (str): The agent performing the action.
            action (str): The tool or method called.
            input_data (Any): Arguments passed to the tool.
            output_data (Any): Result returned by the tool.
            duration_ms (float): Execution time.
            success (bool): Whether the action succeeded.
            intent (str): The agent's stated goal for this step.
            reasoning (str): The "Chain of Thought" leading to this action.
            llm_prompt (str): The actual prompt sent to the LLM (for debugging).
            llm_response (str): The raw response from the LLM.
            state_change (Dict): Diff of the system state before/after the action.
        """
        # Estimate Tokens (Simulated: Char count / 4)
        input_str = str(input_data)
        output_str = str(output_data)
        tokens = (len(input_str) + len(output_str)) // 4
        
        step = {
            "timestamp": datetime.utcnow().isoformat(),
            "agent": agent_name,
            "action": action,
            "context": {
                "intent": intent,
                "reasoning": reasoning,  # Chain of Thought
                "state_change": state_change or {}
            },
            "llm_data": {
                "prompt": llm_prompt or input_str,
                "response": llm_response or output_str
            },
            "input": input_data,
            "output": output_data,
            "duration_ms": duration_ms,
            "tokens": tokens,
            "success": success
        }
        self.trace_data["steps"].append(step)
        self.trace_data["metrics"]["tool_calls"] += 1
        self.trace_data["metrics"]["total_tokens"] += tokens
        if not success:
            self.trace_data["metrics"]["errors"] += 1

    def log_metric(self, trace_id: str, metric_name: str, value: Any):
        """
        Logs a custom metric to the trace data.
        
        Args:
            trace_id (str): The ID of the trace (unused here as we use self.trace_data).
            metric_name (str): The name of the metric.
            value (Any): The value of the metric.
        """
        if "custom_metrics" not in self.trace_data["metrics"]:
            self.trace_data["metrics"]["custom_metrics"] = {}
        
        self.trace_data["metrics"]["custom_metrics"][metric_name] = value

    def evaluate_step(self, agent_name: str, task: str, result: Any) -> float:
        """
        Evaluates the quality of a step (Simulated).
        
        Args:
            agent_name (str): The agent.
            task (str): The task description.
            result (Any): The result.
            
        Returns:
            float: A quality score between 0.0 and 10.0.
        """
        # In a real system, this would use an LLM-as-a-Judge.
        # Here we simulate it based on result success/content.
        score = 8.0 # Baseline
        if isinstance(result, dict) and "error" in result:
            score = 2.0
        elif not result:
            score = 5.0
        return score

    def generate_efficiency_report(self):
        """
        Generates a Markdown report summarizing the operational efficiency of the agents.
        Aggregates data from all traces in the current session.
        """
        # Aggregate steps from all session traces
        all_steps = []
        total_tokens = 0
        
        if self.session_traces:
            for trace in self.session_traces:
                all_steps.extend(trace["steps"])
                total_tokens += trace["metrics"]["total_tokens"]
        else:
            # Fallback if called before end_trace or without session history
            all_steps = self.trace_data["steps"]
            total_tokens = self.trace_data["metrics"]["total_tokens"]

        # Calculate Metrics
        latencies = [s["duration_ms"] for s in all_steps]
        latencies.sort()
        p99_index = int(len(latencies) * 0.99)
        p99_latency = latencies[p99_index] if latencies else 0
        
        complexity = len(all_steps)
        
        # Evaluate against Thresholds
        lat_status = "✅ PASS" if p99_latency <= self.THRESHOLDS["latency_p99_ms"] else f"❌ FAIL (> {self.THRESHOLDS['latency_p99_ms']}ms)"
        tok_status = "✅ PASS" if total_tokens <= self.THRESHOLDS["max_tokens_per_task"] else f"❌ FAIL (> {self.THRESHOLDS['max_tokens_per_task']})"
        comp_status = "✅ PASS" if complexity <= self.THRESHOLDS["max_complexity_steps"] else f"❌ FAIL (> {self.THRESHOLDS['max_complexity_steps']})"

        report = f"# Operational Cost Metrics (Efficiency Report)\n"
        report += f"**Session ID:** `{self.current_trace_id}` (Last Trace)\n"
        report += f"**Total Traces:** {len(self.session_traces)}\n\n"
        
        report += "## 1. System Metrics vs Thresholds (Cumulative)\n"
        report += "| Metric | Measured Value | Threshold | Status |\n"
        report += "| :--- | :--- | :--- | :--- |\n"
        report += f"| **Latency (P99)** | {p99_latency:.2f} ms | {self.THRESHOLDS['latency_p99_ms']} ms | {lat_status} |\n"
        report += f"| **Tokens (Simulated)** | {total_tokens} | {self.THRESHOLDS['max_tokens_per_task']} | {tok_status} |\n"
        report += f"| **Complexity (Steps)** | {complexity} | {self.THRESHOLDS['max_complexity_steps']} | {comp_status} |\n\n"
        
        report += "## 2. Agent Breakdown\n"
        report += "| Agent | Steps | Avg Latency | Tokens |\n"
        report += "| :--- | :--- | :--- | :--- |\n"
        
        agent_stats = {}
        for s in all_steps:
            agent = s["agent"]
            if agent not in agent_stats:
                agent_stats[agent] = {"steps": 0, "latency_sum": 0, "tokens": 0}
            agent_stats[agent]["steps"] += 1
            agent_stats[agent]["latency_sum"] += s["duration_ms"]
            agent_stats[agent]["tokens"] += s["tokens"]
            
        for agent, stats in agent_stats.items():
            avg_lat = stats["latency_sum"] / stats["steps"]
            report += f"| {agent} | {stats['steps']} | {avg_lat:.2f} ms | {stats['tokens']} |\n"

        with open("efficiency_report.md", "w", encoding="utf-8") as f:
            f.write(report)
        self.console.print(f"[bold green]📊 Efficiency Report Generated: efficiency_report.md[/bold green]")

    def check_safety_gate(self, agent_name: str, action: str, target: str) -> bool:
        """
        Implements Safety & Alignment Gates.
        
        This method acts as a firewall for agent actions. It enforces policies
        that agents are not allowed to violate.
        
        Args:
            agent_name (str): The agent attempting the action.
            action (str): The action being attempted.
            target (str): The target of the action.
            
        Returns:
            bool: True if safe to proceed, False if blocked.
        """
        # 1. Scope Safety (Prevent actions outside mock network)
        # We strictly limit operations to the 192.168.1.x subnet to prevent accidental scanning of real networks.
        if "192.168.1." not in target and target != "N/A":
            self.console.print(f"[bold red]⛔ SAFETY GATE BLOCKED: Target {target} is out of scope![/bold red]")
            return False

        # 2. Dangerous Action Safety
        # We block keywords associated with destructive actions.
        dangerous_keywords = ["delete", "format", "shutdown_host", "rm -rf"]
        if any(keyword in action.lower() for keyword in dangerous_keywords):
            self.console.print(f"[bold red]⛔ SAFETY GATE BLOCKED: Action '{action}' contains dangerous keywords![/bold red]")
            return False

        # 3. Alignment Check (Simulated)
        # Ensure agent isn't hallucinating a non-existent protocol
        valid_protocols = ["tcp", "udp", "http", "modbus", "s7", "snmp", "ssh"]
        if action == "scan" and "protocol" in str(target):
             # This is a loose check, just an example of logic
             pass

        return True
