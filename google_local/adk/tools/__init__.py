from typing import Any, Optional, Dict, Callable

class ToolContext:
    """
    Context object passed to tools to support long-running operations and human-in-the-loop.
    """
    def __init__(self, session_id: str = None):
        self.session_id = session_id
        self.tool_confirmation = None

    def request_confirmation(self, hint: str, payload: Dict[str, Any] = None):
        """
        Requests confirmation from the user and persists state.
        """
        print(f"DEBUG: ToolContext.request_confirmation called with hint: {hint}")
        
        # Persist state if session_id is available
        if self.session_id:
            from google_local.adk.sessions import DatabaseSessionService
            session_service = DatabaseSessionService()
            session_service.update_session(self.session_id, {
                "tool_confirmation": {
                    "status": "pending",
                    "hint": hint,
                    "payload": payload
                }
            })
            print(f"DEBUG: Persisted pending confirmation to session {self.session_id}")

        # In a real system, this would pause execution and wait for user input.
        # For this shim, we'll simulate a pending state or auto-approve based on config.
        # For now, we'll just print.
        pass

class Tool:
    def __init__(self, name: str, func: Callable, description: str):
        self.name = name
        self.func = func
        self.description = description
