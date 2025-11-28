from dataclasses import dataclass
from typing import Optional, Any, Dict
from rich.console import Console
from rich.prompt import Prompt

@dataclass
class ToolConfirmation:
    confirmed: bool
    reason: Optional[str] = None

class ToolContext:
    """
    Provides context to a tool execution, including the ability to request
    Human-in-the-Loop (HITL) confirmation.
    """
    def __init__(self, session_id: str = "default", auto_approve: bool = False):
        self.session_id = session_id
        self.auto_approve = auto_approve
        self.tool_confirmation: Optional[ToolConfirmation] = None
        self.console = Console()

    def request_confirmation(self, hint: str, payload: Dict[str, Any] = None) -> None:
        """
        Pauses execution to request user confirmation for a sensitive action.
        
        Args:
            hint (str): A message explaining why confirmation is needed.
            payload (Dict[str, Any]): Data related to the action (e.g., target IP).
        """
        self.console.print(f"\n[bold yellow]⚠️  HITL Request: {hint}[/bold yellow]")
        if payload:
            self.console.print(f"Payload: {payload}")
            
        if self.auto_approve:
            self.console.print("[bold green]✅ Auto-Approved (Flag enabled)[/bold green]")
            response = "y"
        else:
            response = Prompt.ask("Do you authorize this action?", choices=["y", "n"], default="n")
        
        self.tool_confirmation = ToolConfirmation(
            confirmed=(response == "y"),
            reason="User authorized via console" if response == "y" else "User denied"
        )
