class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.total = 0

    def add_expense(self, amount, category=None):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")

        # The dictionary is updated to include the category
        expense = {"amount": amount, "category": category}
        self.expenses.append(expense)
        self.total += amount

    def list_expenses_by_category(self, category):
        # Loop over the expenses and return expenses with the appropriate category
        return [e for e in self.expenses if e.get("category") == category]
