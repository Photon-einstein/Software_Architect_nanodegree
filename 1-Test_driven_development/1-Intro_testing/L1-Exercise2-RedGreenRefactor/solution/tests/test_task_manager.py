from src.task_manager import TaskManager
import pytest


@pytest.fixture
def manager():
    return TaskManager()


def test_add_task_returns_uuid(manager):
    """Existing test to verify setup."""
    task_id = manager.add_task("Test UUID generation")
    assert isinstance(task_id, str)
    assert len(task_id) > 10


def test_get_task_by_id(manager):
    """Verifies valid task retrieval."""
    # Arrange
    expected_title = "Buy Groceries"
    task_id = manager.add_task(expected_title)

    # Act
    retrieved_task = manager.get_task(task_id)

    # Assert
    assert retrieved_task["title"] == expected_title


def test_get_task_nonexistent_returns_none(manager):
    """Verifies that attempting to retrieve a non-existent task returns None."""
    # Act
    retrieved_task = manager.get_task("non-existent-id")

    # Assert
    assert retrieved_task is None
