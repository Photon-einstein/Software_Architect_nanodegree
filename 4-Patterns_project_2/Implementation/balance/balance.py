# balance.py

from transaction.transaction_category import TransactionCategory


class Balance:
    """Singleton to track the balance."""

    _instance = None
    _balance = None
    _observers = None

    def __new__(cls):
        """Initialize the balance. Prevent direct instantiation."""
        if cls._instance is None:
            cls._instance = super(Balance, cls).__new__(cls)
            cls._balance = 0
            cls._observers = []
        return cls._instance

    @classmethod
    def get_instance(cls):
        """Return the single Balance instance."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def register_observer(self, observer):
        """Register an observer to receive balance updates."""
        if observer not in self._observers:
            self._observers.append(observer)

    def notify_observers(self, transaction):
        """Notify observers; transaction is None for direct balance changes."""
        for observer in self._observers:
            observer.update(self.get_balance(), transaction)

    def reset(self):
        """Reset the net balance to zero."""
        self._balance = 0
        self.notify_observers(None)

    def add_income(self, amount):
        """Add income to the balance."""
        self._balance += amount
        self.notify_observers(None)

    def add_expense(self, amount):
        """Subtract expense from the balance."""
        self._balance -= amount
        self.notify_observers(None)

    def apply_transaction(self, transaction):
        """
        Apply a Transaction object to update the balance.

        Args:
            transaction (Transaction): The transaction to apply.
        """
        if transaction.category == TransactionCategory.EXPENSE:
            self._balance -= transaction.amount
        elif transaction.category == TransactionCategory.INCOME:
            self._balance += transaction.amount
        else:
            raise ValueError(
                f"Transaction category '{transaction.category}' not found."
            )
        self.notify_observers(transaction)

    def get_balance(self):
        """Get the current net balance."""
        return self._balance

    def summary(self):
        """Return a summary string of the net balance."""
        return f"Net balance equal to ${self._balance}"
