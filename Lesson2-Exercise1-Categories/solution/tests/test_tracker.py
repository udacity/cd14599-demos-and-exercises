import pytest
from src.tracker import ExpenseTracker

def test_add_expense_stores_amount():
    tracker = ExpenseTracker()
    tracker.add_expense(50)
    assert tracker.expenses[0]['amount'] == 50

def test_add_expense_with_category():    
    tracker = ExpenseTracker()    
    # This call now includes the category argument
    tracker.add_expense(10, category="food")    
    # Asserts that the internal dictionary contains the category key
    assert tracker.expenses[0]['category'] == "food"

def test_list_expenses_by_category_returns_only_requested_category():
    # Arrange
    tracker = ExpenseTracker()
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
