import pytest
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


# TODO: Write test_list_expenses_by_category_returns_only_requested_category here
