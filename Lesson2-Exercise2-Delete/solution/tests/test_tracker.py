import pytest
from src.tracker import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

def test_delete_expense(tracker):    
    # Arrange: Add an expense to delete
    expense_id = tracker.add_expense(20, "entertainment")
    
    # Act: Perform the deletion
    tracker.delete_expense(expense_id)
    
    # Assert: Verify removal and total update
    assert tracker.total == 0
    assert tracker.get_expense(expense_id) is None
