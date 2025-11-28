import logging
from typing import Any, Dict, Optional

class BasePlugin:
    def __init__(self, name: str):
        self.name = name

class LoggingPlugin(BasePlugin):
    """
    Google ADK Logging Plugin.
    """
    def __init__(self):
        super().__init__(name="logging_plugin")
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("adk.logging_plugin")

    def on_agent_start(self, agent_name: str, input_text: str):
        self.logger.info(f"Agent {agent_name} started with input: {input_text}")

    def on_agent_finish(self, agent_name: str, output: Any):
        self.logger.info(f"Agent {agent_name} finished with output: {output}")
