import pytest
from src.tracker import ExpenseTracker


@pytest.fixture
def tracker():
    return ExpenseTracker()


def test_add_expense_stores_amount(tracker):
    # Act
    tracker.add_expense(50)
    # Assert
    assert tracker.expenses[0]["amount"] == 50


def test_add_expense_updates_total(tracker):
    # Act
    tracker.add_expense(10)
    # Assert
    assert tracker.total == 10


def test_add_multiple_expenses(tracker):
    # Act
    tracker.add_expense(10)
    tracker.add_expense(5)
    # Assert
    assert tracker.total == 15


def test_add_expense_with_negative_amount_fails(tracker):
    # Act and Assert
    with pytest.raises(ValueError):
        tracker.add_expense(-10)


def test_add_expense_can_store_category(tracker):
    # Act
    tracker.add_expense(10, category="food")
    # Assert
    assert tracker.expenses[0]["category"] == "food"


def test_list_expenses_by_category_returns_only_requested_category(tracker):
    # Arrange
    tracker.add_expense(10.00, category="food")
    tracker.add_expense(20.00, category="travel")
    tracker.add_expense(5.00, category="food")
    # Act
    results = tracker.list_expenses_by_category("food")
    # Assert
    assert isinstance(results, list)
    assert all(item["category"] == "food" for item in results)
    assert sorted(item["amount"] for item in results) == [5.00, 10.00]


def test_edit_expense(tracker):
    # Arrange
    expense_id = tracker.add_expense(10, category="food")
    # Act
    tracker.edit_expense(expense_id, new_amount=12.50, new_category="dining")
    edited_expense = tracker.get_expense(expense_id)
    # Assert
    assert tracker.total == 12.50
    assert edited_expense["category"] == "dining"


def test_delete_expense(tracker):
    # Arrange: Add an expense to delete
    expense_id = tracker.add_expense(20, "entertainment")

    # Act: Perform the deletion
    tracker.delete_expense(expense_id)

    # Assert: Verify removal and total update
    assert tracker.total == 0
    assert tracker.get_expense(expense_id) is None
