"""
Context Management Module
=========================

This module is responsible for managing the shared context and history of the Multi-Agent System (MAS).
It implements the "Unified History" pattern.
"""

from typing import List, Dict, Any
import datetime
import json
from google_local.adk.sessions import DatabaseSessionService

class ContextManager:
    """
    Manages the shared conversation history and context optimization for the MAS.
    Uses DatabaseSessionService for persistence.
    """
    
    def __init__(self, session_id: str = "mas_session_default"):
        self.session_service = DatabaseSessionService()
        self.session_id = session_id
        
        # Load state from DB
        session_data = self.session_service.get_session(self.session_id)
        self.unified_history: List[Dict[str, Any]] = session_data.get("history", [])
        self.total_tokens_used = session_data.get("tokens", 0)
        self.total_cost_usd = session_data.get("cost", 0.0)
        
        self.PRICE_INPUT_1M = 0.35
        self.PRICE_OUTPUT_1M = 1.05
        self.MAX_CONTEXT_WINDOW = 1000000 
        self.SAFE_WINDOW_THRESHOLD = 0.8

    def _persist(self):
        """Persists current state to the session service."""
        self.session_service.update_session(self.session_id, {
            "history": self.unified_history,
            "tokens": self.total_tokens_used,
            "cost": self.total_cost_usd
        })

    def add_to_history(self, role: str, agent: str, content: str, tool_call: str = None):
        """Appends a new event to the Shared Unified History."""
        entry = {
            "timestamp": datetime.datetime.now().isoformat(),
            "role": role, 
            "agent": agent,
            "content": content,
            "tool_call": tool_call
        }
        self.unified_history.append(entry)
        
        tokens = len(str(content)) // 4
        self.total_tokens_used += tokens
        self._calculate_cost(tokens, is_output=(role == 'assistant'))
        
        self._persist()

    def _calculate_cost(self, tokens: int, is_output: bool):
        """Updates cumulative cost."""
        price = self.PRICE_OUTPUT_1M if is_output else self.PRICE_INPUT_1M
        cost = (tokens / 1_000_000) * price
        self.total_cost_usd += cost

    def optimize_context(self, context_payload: Dict[str, Any], agent_name: str) -> str:
        """Optimizes the context payload for a specific agent."""
        return json.dumps(context_payload, indent=2)

    def get_metrics(self) -> Dict[str, Any]:
        """Returns the current usage metrics."""
        return {
            "total_tokens": self.total_tokens_used,
            "total_cost_usd": round(self.total_cost_usd, 4),
            "history_length": len(self.unified_history)
        }

    def get_recent_history(self, limit: int = 5) -> List[Dict[str, Any]]:
        """Retrieves the most recent events from the history."""
        return self.unified_history[-limit:]
