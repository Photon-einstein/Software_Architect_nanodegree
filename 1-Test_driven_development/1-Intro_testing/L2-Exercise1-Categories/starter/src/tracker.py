class ExpenseTracker:
    def __init__(self):
        # The tracker stores records in a list
        self.expenses = []
        self.total = 0

    def add_expense(self, amount):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        # Current implementation only handles amount
        expense = {"amount": amount}
        self.expenses.append(expense)
        self.total += amount
