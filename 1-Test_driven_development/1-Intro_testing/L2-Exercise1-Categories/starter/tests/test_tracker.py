import pytest  # pyright: ignore[reportMissingImports]
from src.tracker import ExpenseTracker


def test_add_expense_stores_amount():
    # Arrange
    tracker = ExpenseTracker()

    # Act
    tracker.add_expense(50)

    # Assert
    assert tracker.expenses[0]["amount"] == 50


def test_add_expense_updates_total():
    # Arrange
    tracker = ExpenseTracker()

    # Act
    tracker.add_expense(10)

    # Assert
    assert tracker.total == 10


def test_add_multiple_expenses():
    # Arrange
    tracker = ExpenseTracker()

    # Act
    tracker.add_expense(10)
    tracker.add_expense(5)

    # Assert
    assert tracker.total == 15


def test_add_expense_with_negative_amount_fails():
    # Arrange
    tracker = ExpenseTracker()

    # Act and Assert
    with pytest.raises(ValueError):
        tracker.add_expense(-10)


# TODO: Write test_add_expense_can_store_category here
def test_add_expense_stores_amount_and_category():
    # Arrange
    tracker = ExpenseTracker()

    # Act
    expenseCategory = "Utility"
    tracker.add_expense(50, expenseCategory)

    # Assert
    assert tracker.expenses[0]["amount"] == 50
    assert tracker.expenses[0]["category"] == expenseCategory


# TODO: Write test_list_expenses_by_category_returns_only_requested_category here
def test_list_expenses_by_category_returns_only_requested_category():
    # Arrange
    tracker = ExpenseTracker()

    # Act
    expenseCategory1 = "Utility"
    expenseCategory2 = "Water"
    tracker.add_expense(50, expenseCategory1)
    tracker.add_expense(100, expenseCategory1)
    tracker.add_expense(5, expenseCategory2)
    tracker.add_expense(15, expenseCategory2)

    # Assert
    list_expenses = tracker.list_expenses_by_category(expenseCategory2)
    assert isinstance(list_expenses, list)
    assert all(item["category"] == expenseCategory2 for item in list_expenses)
    assert len(list_expenses) == 2
    assert sorted(item["amount"] for item in list_expenses) == [5, 15]
