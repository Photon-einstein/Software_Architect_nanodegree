class ExpenseTracker:
    def __init__(self):
        # The tracker stores records in a list
        self.expenses = []
        self.total = 0

    def add_expense(self, amount, category=""):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        # Current implementation only handles amount
        expense = {"amount": amount, "category": category}
        self.expenses.append(expense)
        self.total += amount

    def list_expenses_by_category(self, category):
        if category == "":
            raise ValueError("Input category cannot be empty.")
        return [e for e in self.expenses if e.get("category") == category]
