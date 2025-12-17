class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category=None):
        # The dictionary is updated to include the category
        expense = {
            "amount": amount,
            "category": category
        }
        self.expenses.append(expense)
