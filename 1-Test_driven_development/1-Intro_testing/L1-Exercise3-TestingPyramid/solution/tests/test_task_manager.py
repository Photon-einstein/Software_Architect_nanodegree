# We use a mock 'By' class here (defined in conftest.py) so you don't need Selenium installed.
from tests.conftest import By


def test_unit_task_manager_can_mark_task_complete(manager):
    """
    1. Unit Test: Tests the logic of the TaskManager class in isolation.
    """
    # Arrange: Add a task to the manager
    task_id = manager.add_task("Unit Test Task")

    # Act: Mark the task as complete
    manager.mark_complete(task_id)

    # Assert: Verify the internal state change
    assert manager.get_task(task_id)["completed"] is True


def test_integration_api_creates_task(test_app, manager):
    """
    2. Integration Test: Tests the connection between the API and the TaskManager.
    """
    # Arrange: Define the API payload
    api_payload = {"title": "Integration Test Task"}

    # Act: Send a POST request to the API
    response = test_app.post("/api/task", json=api_payload)

    # Assert 1: Check the HTTP contract
    assert response.status_code == 201

    # Assert 2: Check the persistence/logic integration
    # We check the task exists directly in the manager object
    assert manager.get_task_by_title(api_payload["title"]) is not None


def test_e2e_user_can_create_task_via_ui(selenium_driver):
    """
    3. E2E Test: Simulates a full user workflow via the UI.
    """
    # Arrange & Act: User types text into an input and clicks a button
    selenium_driver.get("http://localhost:8000/tasks")
    task_title = "E2E Test Task Title"

    input_field = selenium_driver.find_element(By.ID, "new-task-input")
    input_field.send_keys(task_title)

    add_button = selenium_driver.find_element(By.ID, "add-button")
    add_button.click()

    # Assert: Check the final result as a user would see it on the page.
    assert task_title in selenium_driver.find_element(By.ID, "task-list").text
