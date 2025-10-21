"""
Implement a minimal in-memory TodoList.

Requirements (must-haves)
-------------------------
- IDs start at 1 and increment by 1 for each added item.
- .add_item(text: str) -> dict
    - Trim whitespace. If empty after trim, raise ValueError.
    - Returns the created item dict: {"id": int, "text": str, "done": bool}
- .complete_item(item_id: int) -> None
    - If not found, raise KeyError.
- .remove_item(item_id: int) -> None
    - If not found, raise KeyError.
- .list_pending() -> list[dict]
    - Return a list of items where done == False, in insertion order.
- .stats() -> dict
    - Return {"total": int, "done": int, "pending": int}

Constraints
-----------
- Keep the implementation small and readable (≈ 40 lines or less).
- No I/O (no prints, no files); just data and methods.
- Store items in memory only (e.g., a list).

Tips for implementation
-----------------------
- Keep a `self._next_id` counter.
- Use simple dicts for items: {"id": int, "text": str, "done": bool}.
- Consider small helper methods if it stays simple.

You will also create tests in test_todo.py.
"""

# Write your TodoList class here.
# Start with a stub so tests import will work, then iterate.

class TodoList:
    pass
