"""Ebbinghaus forgetting curve memory store."""
import time
import math
from typing import Dict, Any, List

class TemporalMemoryStore:
    def __init__(self, decay_rate: float = 0.05, retention_threshold: float = 0.2):
        self.decay_rate = decay_rate
        self.retention_threshold = retention_threshold
        self.memories: Dict[str, Dict[str, Any]] = {}

    def add_memory(self, key: str, value: Any, strength: float = 1.0) -> None:
        self.memories[key] = {
            "value": value,
            "strength": strength,
            "stability": 1.0,
            "timestamp": time.time(),
            "access_count": 0
        }

    def access_memory(self, key: str) -> Any:
        if key not in self.memories:
            return None
        m = self.memories[key]
        m["access_count"] += 1
        m["stability"] *= 1.5  # Increase stability on recall
        m["timestamp"] = time.time()
        return m["value"]

    def cleanup_forgotten(self) -> List[str]:
        now = time.time()
        evicted = []
        for key, m in list(self.memories.items()):
            dt = now - m["timestamp"]
            current_retention = m["strength"] * math.exp(-self.decay_rate * dt / m["stability"])
            if current_retention < self.retention_threshold:
                evicted.append(key)
                del self.memories[key]
        return evicted
