from typing import List, Any, Optional, Dict
import abc

class Agent(abc.ABC):
    """
    Google ADK Agent Interface.
    """
    def __init__(self, name: str, instruction: str, tools: List[Any] = None, model: Any = None):
        print(f"DEBUG: Using Local Shim Agent for {name}")
        self.name = name
        self.instruction = instruction
        self.tools = tools or []
        self.model = model

    def add_tool(self, tool: Any):
        self.tools.append(tool)

    @abc.abstractmethod
    def run(self, input_text: str, context: Optional[Dict[str, Any]] = None, **kwargs) -> Any:
        pass

class Model(abc.ABC):
    @abc.abstractmethod
    def generate_content(self, prompt: str) -> str:
        pass

class Tool:
    def __init__(self, name: str, func: Any, description: str):
        self.name = name
        self.func = func
        self.description = description
