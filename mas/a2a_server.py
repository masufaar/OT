import os
from google_local.adk.a2a import to_a2a
from mas.orchestrator import RootAgent
from mas.memory import LongTermMemory
from mas.observability import QualityManager
from mas.context import ContextManager

def create_app():
    """
    Creates the A2A application for the RootAgent.
    """
    # Initialize Dependencies
    memory = LongTermMemory()
    quality = QualityManager()
    context = ContextManager()
    
    # Initialize RootAgent
    root_agent = RootAgent(
        memory_system=memory,
        quality_manager=quality,
        context_manager=context,
        auto_approve=True # Auto-approve for A2A context usually, or handle via protocol
    )
    
    # Expose via A2A
    app = to_a2a(root_agent, port=8000)
    return app

if __name__ == "__main__":
    app = create_app()
    if hasattr(app, 'run'):
        app.run()
