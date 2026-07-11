import pytest  # pyright: ignore[reportMissingImports]

# We use a mock 'By' class here (defined in conftest.py) so you don't need Selenium installed.
from tests.conftest import By


def test_unit_task_manager_can_mark_task_complete(manager):
    """
    Tests the logic of the TaskManager class in isolation.
    (It doesn't talk to a database or API.)
    """
    # Arrange: Add a task to the manager
    task_id = manager.add_task("Unit Test Task")

    # Act: Mark the task as complete (Assume a .mark_complete(task_id) method exists)
    manager.mark_complete(task_id)

    # Assert: Verify the internal state change
    # Write the final assertion here. Hint: Check the task's 'completed' property.
    assert manager.get_task(task_id)["completed"] == True


# Assume 'test_app' is a fixture that lets you make requests to the API server
def test_integration_api_creates_task(test_app, manager):
    """
    Tests the API endpoint and its connection to the TaskManager logic layer.
    (Checks the 'plumbing' between the API and the Unit.)
    """
    # Arrange: Define the API payload
    api_payload = {"title": "Integration Test Task"}

    # Act: Send a POST request to the API
    response = test_app.post("/api/task", json=api_payload)

    # Assert 1: Check the HTTP contract
    assert response.status_code == 201

    # Assert 2: Check the persistence/logic integration
    # TODO: Write the assertion to confirm the task now exists in the manager's state.
    assert manager.get_task_by_title(api_payload["title"]) != None


# Assume 'selenium_driver' is a fixture that opens a browser
def test_e2e_user_can_create_task_via_ui(selenium_driver):
    """
    Simulates a full user workflow: navigating, inputting data, and viewing the result.
    (This is the slowest, highest-confidence test.)
    """
    # Arrange & Act: User types text into an input and clicks a button
    # Assume driver has methods like .get() and .find_element()
    selenium_driver.get("http://localhost:8000/tasks")
    task_title = "E2E Test Task Title"

    input_field = selenium_driver.find_element(By.ID, "new-task-input")
    input_field.send_keys(task_title)

    add_button = selenium_driver.find_element(By.ID, "add-button")
    add_button.click()

    # Assert: Check the final result as a user would see it on the page.
    # Write the assertion to confirm the task title is visible in the task list element.
    assert selenium_driver.find_element(By.ID, "task-list").text == task_title
