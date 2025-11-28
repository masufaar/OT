from typing import Any, Dict, Optional, List
from ..agents import Agent
from ..sessions import InMemorySessionService

class Runner:
    """
    Google ADK Runner Interface.
    """
    def __init__(self, agent: Agent, session_service: Any = None, plugins: List[Any] = None):
        self.agent = agent
        self.session_service = session_service or InMemorySessionService()
        self.plugins = plugins or []

    def run(self, input_text: str, session_id: str = "default") -> Any:
        # Notify plugins start
        for plugin in self.plugins:
            if hasattr(plugin, 'on_agent_start'):
                plugin.on_agent_start(self.agent.name, input_text)

        # Run agent
        result = self.agent.run(input_text)
        
        # Notify plugins finish
        for plugin in self.plugins:
            if hasattr(plugin, 'on_agent_finish'):
                plugin.on_agent_finish(self.agent.name, result)
                
        return result
