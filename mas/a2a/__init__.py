from typing import List, Any, Optional, Dict, Callable
from dataclasses import dataclass, field
import uuid
from datetime import datetime

@dataclass
class Message:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    source: str = ""
    target: str = ""
    topic: str = ""
    payload: Dict[str, Any] = field(default_factory=dict)
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())

class Bus:
    """
    Simple In-Memory Message Bus for A2A communication.
    """
    def __init__(self):
        self._subscribers: Dict[str, List[Callable[[Message], None]]] = {}

    def subscribe(self, topic: str, callback: Callable[[Message], None]):
        if topic not in self._subscribers:
            self._subscribers[topic] = []
        self._subscribers[topic].append(callback)

    def publish(self, message: Message):
        if message.topic in self._subscribers:
            for callback in self._subscribers[message.topic]:
                callback(message)
        
        # Also support wildcard '*' subscription
        if "*" in self._subscribers:
             for callback in self._subscribers["*"]:
                callback(message)
