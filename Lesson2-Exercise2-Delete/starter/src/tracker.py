class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.total = 0
        self._next_id = 1

    def add_expense(self, amount, category):
        expense_id = self._next_id
        expense = {
            "id": expense_id,
            "amount": amount, 
            "category": category
        }
        self.expenses.append(expense)
        self.total += amount
        self._next_id += 1
        return expense_id

    def get_expense(self, expense_id):
        # Helper to find a specific expense by ID
        return next((e for e in self.expenses if e["id"] == expense_id), None)
