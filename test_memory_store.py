import tempfile
from pathlib import Path

from memory_store import MemoryStore


def test_round_trip_and_search() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "memory.json"
        store = MemoryStore(path)
        store.add(
            {
                "id": "M-001",
                "topic": "context",
                "content": "persistent project memory",
                "source": "test",
                "status": "observation",
            }
        )
        restored = MemoryStore(path)
        matches = restored.search("persistent memory")
        assert matches
        assert matches[0]["id"] == "M-001"
