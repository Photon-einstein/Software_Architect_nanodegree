import unittest
from unittest.mock import Mock, call, patch

from balance.balance import Balance
from balance.balance_observer import LowBalanceAlertObserver, PrintObserver
from main import main
from transaction.transaction import Transaction
from transaction.transaction_category import TransactionCategory


class TestLowBalanceAlertObserver(unittest.TestCase):

    def setUp(self):
        self.balance = Balance.get_instance()
        self.balance.reset()

    def test_alert_triggers_on_low_balance(self):
        observer = LowBalanceAlertObserver(threshold=50)
        self.balance.register_observer(observer)

        self.balance.apply_transaction(
            Transaction(
                100,
                TransactionCategory.INCOME)
            )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(
                60,
                TransactionCategory.EXPENSE)
            )
        self.assertTrue(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(
                100,
                TransactionCategory.INCOME)
            )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(
                60,
                TransactionCategory.EXPENSE)
            )
        self.assertFalse(observer.alert_triggered)

        self.balance.apply_transaction(
            Transaction(
                60,
                TransactionCategory.EXPENSE)
            )
        self.assertTrue(observer.alert_triggered)


class TestBalanceNotifications(unittest.TestCase):
    def setUp(self):
        for attribute in ("_instance", "_observers", "_balance"):
            patcher = patch.object(Balance, attribute, None)
            patcher.start()
            self.addCleanup(patcher.stop)
        self.balance = Balance.get_instance()

    def test_direct_changes_notify_observers(self):
        observer = Mock()
        self.balance.register_observer(observer)
        self.balance.register_observer(observer)

        self.balance.add_income(100)
        self.balance.add_expense(40)
        self.balance.reset()

        self.assertEqual(
            observer.update.call_args_list,
            [call(100, None), call(60, None), call(0, None)],
        )

    def test_alert_and_print_output(self):
        self.balance.register_observer(
            LowBalanceAlertObserver(
                threshold=50
                )
            )
        self.balance.register_observer(PrintObserver())
        with patch("builtins.print") as print_mock:
            self.balance.apply_transaction(
                Transaction(
                    50,
                    TransactionCategory.INCOME
                )
            )
            self.assertFalse(
                any(
                    "Low balance alert" in str(c)
                    for c in print_mock.call_args_list
                )
            )
            print_mock.reset_mock()
            self.balance.apply_transaction(
                Transaction(
                    10,
                    TransactionCategory.EXPENSE
                )
            )
            print_mock.assert_any_call("Low balance alert: $40 is below $50")
            print_mock.assert_any_call("Expense: $10")
            print_mock.assert_any_call("Balance updated: $40")
            print_mock.reset_mock()
            self.balance.reset()
            print_mock.assert_any_call("Balance updated: $0")

    def test_invalid_transaction_does_not_notify(self):
        observer = Mock()
        self.balance.register_observer(observer)

        with self.assertRaises(ValueError):
            self.balance.apply_transaction(Transaction(10, "invalid"))

        observer.update.assert_not_called()
        self.assertEqual(self.balance.get_balance(), 0)

    def test_main_registers_observers_and_processes_transactions(self):
        with patch("builtins.print") as print_mock:
            main()

        self.assertEqual(self.balance.get_balance(), 175)
        print_mock.assert_any_call("Low balance alert: $100 is below $200")
        print_mock.assert_any_call("Balance updated: $1375")
        print_mock.assert_any_call("Balance updated: $175")


if __name__ == "__main__":
    unittest.main()
