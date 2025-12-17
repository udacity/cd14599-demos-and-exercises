class ExpenseTracker:
    def __init__(self):
        # The tracker stores records in a list
        self.expenses = []

    def add_expense(self, amount):
        # Current implementation only handles amount
        expense = {"amount": amount}
        self.expenses.append(expense)
