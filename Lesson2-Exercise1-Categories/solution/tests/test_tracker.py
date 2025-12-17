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
