from typing import Any, Dict, Optional
from ..agents import Agent

class RemoteA2aAgent(Agent):
    """
    Google ADK Remote A2A Agent.
    """
    def __init__(self, name: str, description: str, agent_card: str):
        super().__init__(name=name, instruction=description)
        self.description = description
        self.agent_card_url = agent_card

    def run(self, input_text: str, context: Optional[Dict[str, Any]] = None, **kwargs) -> Any:
        print(f"DEBUG: RemoteA2aAgent {self.name} called with input: {input_text}")
        return f"Remote A2A response for: {input_text}"

def to_a2a(agent: Agent, port: int = 8000) -> Any:
    """
    Exposes an agent via A2A protocol.
    Returns a mock FastAPI app.
    """
    print(f"DEBUG: Exposing agent {agent.name} on port {port} via A2A")
    class MockFastAPIApp:
        def run(self):
            print(f"Starting A2A server on port {port}...")
    return MockFastAPIApp()

AGENT_CARD_WELL_KNOWN_PATH = "/.well-known/agent-card.json"
