import pytest
from .todo import TodoList

# 🧪 Your job:
# - Write tests that cover all requirements in todo.py's docstring.
# - Start with the most basic path (add → stats → list_pending).
# - Then cover errors (empty text, missing id), and edge cases.
# - Aim for 5–7 short tests in total.
#
# Suggested structure to get started:
#
# def test_add_returns_item_and_increments_id():
#     todos = TodoList()
#     first = todos.add_item(" buy milk ")
#     assert first == {"id": 1, "text": "buy milk", "done": False}
#     second = todos.add_item("walk dog")
#     assert second["id"] == 2
#
# def test_complete_and_stats_and_list_pending():
#     todos = TodoList()
#     todos.add_item("a"); todos.add_item("b")
#     todos.complete_item(1)
#     assert todos.stats() == {"total": 2, "done": 1, "pending": 1}
#     assert [i["id"] for i in todos.list_pending()] == [2]
#
# def test_remove_and_missing_ids():
#     todos = TodoList()
#     todos.add_item("a")
#     todos.remove_item(1)
#     with pytest.raises(KeyError):
#         todos.complete_item(1)
#
# def test_empty_text_raises():
#     todos = TodoList()
#     with pytest.raises(ValueError):
#         todos.add_item("   ")
#
# When you have your plan, delete the skip below and add real tests.

pytest.skip("TODO: implement TodoList and write tests following the requirements")
