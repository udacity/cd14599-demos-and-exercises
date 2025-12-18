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

    def list_expenses_by_category(self, category):
        # Loop over the expenses and return expenses with the appropriate category
        return [e for e in self.expenses if e.get("category") == category]
