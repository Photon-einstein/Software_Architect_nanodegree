import uuid


class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    @property
    def total(self):
        return sum([e["amount"] for e in self.expenses])

    # ------------- Create -------------
    def add_expense(self, amount, category=None):
        if amount <= 0:
            raise ValueError("Expense amount must be positive.")
        expense_id = str(uuid.uuid4())
        expense = {"id": expense_id, "amount": amount, "category": category}
        self.expenses.append(expense)
        return expense_id

    # ------------- Read -------------
    def list_expenses_by_category(self, category):
        return [e for e in self.expenses if e.get("category") == category]

    def get_expense(self, expense_id):
        return next((e for e in self.expenses if e["id"] == expense_id), None)

    # ------------- Update -------------
    def edit_expense(self, expense_id, new_amount=None, new_category=None):
        expense = self.get_expense(expense_id)
        if expense:
            if new_amount is not None:
                expense["amount"] = new_amount
            if new_category is not None:
                expense["category"] = new_category

    # ------------- Delete -------------
