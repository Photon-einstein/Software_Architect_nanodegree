from src.task_manager import TaskManager
import pytest  # pyright: ignore[reportMissingImports]


# Fixture to ensure a fresh TaskManager for each test
@pytest.fixture
def manager():
    return TaskManager()


# Existing test to verify setup (should pass)
def test_add_task_returns_uuid(manager):
    task_id = manager.add_task("Test UUID generation")
    assert isinstance(task_id, str)
    assert len(task_id) > 10  # Basic check for UUID-like string


def test_get_task_by_id(manager):
    task_text = "Test UUID generation"
    task_id = manager.add_task(task_text)
    task_retrieved = manager.get_task_by_id(task_id)
    assert task_retrieved == task_text


def test_get_task_nonexistent_returns_none(manager):
    task_id_not_existent = "Oops"
    task_retrieved = manager.get_task_by_id(task_id_not_existent)
    assert task_retrieved == None
