"""Command line interface for temporal-memory-decay."""
from .memory import TemporalMemoryStore

def main():
    store = TemporalMemoryStore()
    store.add_memory("user_name", "Ejaj")
    print("Stored memory:", store.access_memory("user_name"))

if __name__ == "__main__":
    main()
