import pytest
from src.tracker import ExpenseTracker

def test_add_expense_stores_amount():
    tracker = ExpenseTracker()
    tracker.add_expense(50)
    assert tracker.expenses[0]['amount'] == 50

# TODO: Write test_add_expense_can_store_category here


# TODO: Write test_list_expenses_by_category_returns_only_requested_category here
