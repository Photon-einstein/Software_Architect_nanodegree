from abc import ABC, abstractmethod

from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class Command(ABC):
    @abstractmethod
    def execute(self):
        """Perform the command."""

    @abstractmethod
    def undo(self):
        """Reverse the command."""


class TransactionCommand(Command):
    """Apply a transaction and reverse it with an opposite transaction."""

    def __init__(self, balance, transaction):
        if transaction.category == TransactionCategory.INCOME:
            opposite = TransactionCategory.EXPENSE
        elif transaction.category == TransactionCategory.EXPENSE:
            opposite = TransactionCategory.INCOME
        else:
            raise ValueError(
                f"Transaction category '{transaction.category}' not found."
            )

        self._balance = balance
        self._transaction = Transaction(transaction.amount, transaction.category)
        self._reverse = Transaction(transaction.amount, opposite)
        self._executed = False

    def execute(self):
        if self._executed:
            raise RuntimeError("Transaction command has already been executed.")
        self._balance.apply_transaction(self._transaction)
        self._executed = True

    def undo(self):
        if not self._executed:
            raise RuntimeError("Transaction command has not been executed.")
        self._balance.apply_transaction(self._reverse)
        self._executed = False


class TransactionHistory:
    """Execute commands and undo them in last-in, first-out order."""

    def __init__(self):
        self._commands = []

    def execute(self, command):
        command.execute()
        self._commands.append(command)

    def undo_last(self):
        if not self._commands:
            raise RuntimeError("No transaction to undo.")
        self._commands[-1].undo()
        self._commands.pop()
