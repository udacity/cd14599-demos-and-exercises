import pytest
from src.tracker import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

# TODO: Write test_delete_expense(tracker) here
# 1. Add an expense and capture the ID
# 2. Call tracker.delete_expense(expense_id)
# 3. Assert tracker.total is updated to 0
# 4. Assert tracker.get_expense(expense_id) returns None
