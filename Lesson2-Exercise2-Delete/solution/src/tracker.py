class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.total = 0
        self._next_id = 1

    def add_expense(self, amount, category):
        expense_id = self._next_id
        expense = {"id": expense_id, "amount": amount, "category": category}
        self.expenses.append(expense)
        self.total += amount
        self._next_id += 1
        return expense_id

    def get_expense(self, expense_id):
        return next((e for e in self.expenses if e["id"] == expense_id), None)

    def delete_expense(self, expense_id):
        # Locate the expense to ensure it exists before removal
        expense_to_delete = self.get_expense(expense_id)
        if expense_to_delete:
            # Subtract the amount from total to maintain integrity
            self.total -= expense_to_delete["amount"]
            self.expenses.remove(expense_to_delete)
