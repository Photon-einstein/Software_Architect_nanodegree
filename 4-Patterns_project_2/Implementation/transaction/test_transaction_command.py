import unittest
from unittest.mock import Mock, patch

from balance.balance import Balance
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory
from transaction.transaction_command import (
    TransactionCommand,
    TransactionHistory,
)


class TestTransactionCommand(unittest.TestCase):
    def setUp(self):
        for attribute in ("_instance", "_observers", "_balance"):
            patcher = patch.object(Balance, attribute, None)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.balance = Balance.get_instance()
        self.history = TransactionHistory()

    def test_undo_income_and_expense_in_reverse_order(self):
        observer = Mock()
        self.balance.register_observer(observer)
        self.history.execute(
            TransactionCommand(
                self.balance, Transaction(100, TransactionCategory.INCOME)
            )
        )
        self.history.execute(
            TransactionCommand(
                self.balance, Transaction(40, TransactionCategory.EXPENSE)
            )
        )
        self.assertEqual(self.balance.get_balance(), 60)

        self.history.undo_last()
        self.assertEqual(self.balance.get_balance(), 100)
        self.assertEqual(
            observer.update.call_args.args[1].category,
            TransactionCategory.INCOME,
        )
        self.history.undo_last()
        self.assertEqual(self.balance.get_balance(), 0)
        self.assertEqual(
            observer.update.call_args.args[1].category,
            TransactionCategory.EXPENSE,
        )
        self.assertEqual(observer.update.call_count, 4)

    def test_empty_history_and_invalid_command(self):
        with self.assertRaises(RuntimeError):
            self.history.undo_last()
        with self.assertRaises(ValueError):
            TransactionCommand(self.balance, Transaction(10, "invalid"))
        with self.assertRaises(RuntimeError):
            self.history.undo_last()
        self.assertEqual(self.balance.get_balance(), 0)

    def test_command_state_and_transaction_snapshot(self):
        transaction = Transaction(30, TransactionCategory.INCOME)
        command = TransactionCommand(self.balance, transaction)
        with self.assertRaises(RuntimeError):
            command.undo()
        self.history.execute(command)
        with self.assertRaises(RuntimeError):
            self.history.execute(command)
        transaction.amount = 99
        transaction.category = TransactionCategory.EXPENSE
        self.history.undo_last()
        self.assertEqual(self.balance.get_balance(), 0)
        with self.assertRaises(RuntimeError):
            self.history.undo_last()


if __name__ == "__main__":
    unittest.main()
