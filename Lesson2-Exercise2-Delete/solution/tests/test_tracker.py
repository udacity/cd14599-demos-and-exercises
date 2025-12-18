import pytest
from src.tracker import ExpenseTracker

@pytest.fixture
def tracker():
    return ExpenseTracker()

def test_add_expense_stores_amount(tracker):
    tracker.add_expense(50)
    assert tracker.expenses[0]['amount'] == 50

def test_add_expense_with_category(tracker):
    tracker.add_expense(10, category="food")
    assert tracker.expenses[0]['category'] == "food"

def test_list_expenses_by_category_returns_only_requested_category(tracker):
    # Arrange
    tracker.add_expense(10.00, category="food")
    tracker.add_expense(20.00, category="travel")
    tracker.add_expense(5.00,  category="food")

    # Act
    results = tracker.list_expenses_by_category("food")

    # Assert
    assert isinstance(results, list)
    # Only "food" expenses should be returned
    assert all(item["category"] == "food" for item in results)
    # Amounts for the returned items should match the two "food" entries
    assert sorted(item["amount"] for item in results) == [5.00, 10.00]

def test_delete_expense(tracker):    
    # Arrange: Add an expense to delete
    expense_id = tracker.add_expense(20, "entertainment")
    
    # Act: Perform the deletion
    tracker.delete_expense(expense_id)
    
    # Assert: Verify removal and total update
    assert tracker.total == 0
    assert tracker.get_expense(expense_id) is None
