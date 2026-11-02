"""Unit tests for TemporalMemoryStore."""
import unittest
import time
from temporal_memory_decay.memory import TemporalMemoryStore

class TestTemporalMemory(unittest.TestCase):
    def test_decay_and_retention(self):
        store = TemporalMemoryStore(decay_rate=10.0, retention_threshold=0.5)
        store.add_memory("ephemeral", "trivia")
        time.sleep(0.15)
        evicted = store.cleanup_forgotten()
        self.assertIn("ephemeral", evicted)

if __name__ == "__main__":
    unittest.main()
