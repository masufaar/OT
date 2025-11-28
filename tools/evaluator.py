"""
Evaluator Script
================

This script runs the Multi-Agent System against a defined evaluation set (`integration.evalset.json`)
and calculates quality metrics based on `test_config.json`.

It serves as the "Proactive Testing" suite recommended in Day 4 best practices.
"""

import json
import os
import sys
from typing import List, Dict, Any
from rich.console import Console
from rich.table import Table

# Add parent directory to path to import mas modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from mas.orchestrator import RootAgent
from mas.memory import LongTermMemory
from mas.observability import QualityManager
from mas.context import ContextManager
from agents.network_scanner import NetworkScanner
from agents.port_scanner import PortScanner
from agents.service_scanner import ServiceScanner
from agents.web_scanner import WebScanner

class Evaluator:
    def __init__(self, config_path: str = "tests/test_config.json", evalset_path: str = "tests/integration.evalset.json"):
        self.console = Console()
        self.config = self._load_json(config_path)
        self.evalset = self._load_json(evalset_path)
        
        # Initialize System
        self.memory = LongTermMemory("mas_test.db") # Use a test DB
        self.quality = QualityManager(log_dir="tests/logs", golden_set_dir="tests/golden_sets")
        self.context = ContextManager()
        self.root_agent = RootAgent(self.memory, self.quality, self.context)
        
        # Agent Map
        self.agents = {
            "NetworkScanner": NetworkScanner(use_mock=True),
            "PortScanner": PortScanner(use_mock=True),
            "ServiceScanner": ServiceScanner(use_mock=True),
            "WebScanner": WebScanner(use_mock=True)
        }
        
        # Mock HITL for automation
        # We monkey-patch the ToolContext to auto-approve requests during testing.
        from mas.tool_context import ToolContext, ToolConfirmation
        
        def mock_request_confirmation(self_ctx, hint: str, payload: Dict[str, Any] = None):
            self.console.print(f"[yellow]🧪 Auto-Approving HITL Request: {hint}[/yellow]")
            self_ctx.tool_confirmation = ToolConfirmation(confirmed=True, reason="Auto-Approved by Evaluator")
            
        ToolContext.request_confirmation = mock_request_confirmation

    def _load_json(self, path: str) -> Any:
        with open(path, "r") as f:
            return json.load(f)

    def run_evaluation(self):
        self.console.print("[bold blue]🧪 Starting MAS Evaluation...[/bold blue]")
        
        results = []
        total_score = 0
        
        for case in self.evalset:
            case_id = case["id"]
            prompt = case["prompt"]
            expected_tools = case["expected_tools"]
            keywords = case["golden_answer_keywords"]
            
            self.console.print(f"\nRunning Test Case: [bold]{case_id}[/bold]")
            self.console.print(f"Prompt: {prompt}")
            
            # 1. Select Agent (Simplified for this script)
            # In a real eval, the RootAgent would select the tool via LLM.
            # Here we pick the first expected tool to test execution.
            agent_name = expected_tools[0]
            agent = self.agents.get(agent_name)
            
            if not agent:
                self.console.print(f"[red]Agent {agent_name} not found![/red]")
                continue
                
            # 2. Execute Task
            # Determine target IP based on agent type and prompt
            target_ip = "192.168.1.10" # Default single target
            if "NetworkScanner" in agent_name:
                target_ip = "192.168.1.0/24"
            elif "192.168.1.10" in prompt:
                target_ip = "192.168.1.10"
            elif "192.168.1.20" in prompt:
                target_ip = "192.168.1.20"
            
            try:
                result = self.root_agent.run_agent_task(agent, prompt, target_ip)
                result_str = str(result)
                
                # 3. Calculate Scores
                # Response Match: Check for keywords
                matches = sum(1 for k in keywords if k.lower() in result_str.lower())
                match_score = matches / len(keywords) if keywords else 1.0
                
                # Tool Trajectory: Did we use the right tool? (Yes, because we forced it, but we log it)
                trajectory_score = 1.0 # Placeholder
                
                score = (match_score + trajectory_score) / 2
                total_score += score
                
                status = "PASS" if score >= self.config["thresholds"]["response_match_score"] else "FAIL"
                color = "green" if status == "PASS" else "red"
                
                self.console.print(f"[{color}]Status: {status} | Score: {score:.2f}[/{color}]")
                
                results.append({
                    "id": case_id,
                    "status": status,
                    "score": score,
                    "output_snippet": result_str[:100] + "..."
                })
                
            except Exception as e:
                self.console.print(f"[red]Error: {e}[/red]")
                results.append({"id": case_id, "status": "ERROR", "error": str(e)})

        # Summary
        self._print_summary(results)

    def _print_summary(self, results: List[Dict]):
        table = Table(title="Evaluation Summary")
        table.add_column("Test ID", style="cyan")
        table.add_column("Status", style="bold")
        table.add_column("Score")
        table.add_column("Output")
        
        for r in results:
            status_style = "green" if r.get("status") == "PASS" else "red"
            table.add_row(
                r["id"], 
                f"[{status_style}]{r.get('status')}[/{status_style}]", 
                f"{r.get('score', 0):.2f}", 
                r.get("output_snippet", r.get("error", ""))
            )
            
        self.console.print("\n")
        self.console.print(table)
        
        # Save Report
        with open("tests/eval_report.json", "w") as f:
            json.dump(results, f, indent=2)
            
        self.console.print(f"[bold blue]Report saved to tests/eval_report.json[/bold blue]")

if __name__ == "__main__":
    evaluator = Evaluator()
    evaluator.run_evaluation()
