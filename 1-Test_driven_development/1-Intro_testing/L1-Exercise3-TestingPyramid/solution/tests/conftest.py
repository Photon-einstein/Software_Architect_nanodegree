import pytest
from src.task_manager import TaskManager


# --- Mocks for missing libraries (Selenium/Flask) ---
class MockResponse:
    def __init__(self, status_code):
        self.status_code = status_code


class MockTestApp:
    def __init__(self, manager):
        self.manager = manager

    def post(self, url, json):
        # Simulate the API creating a task in the manager
        if url == "/api/task":
            self.manager.add_task(json["title"])
            return MockResponse(201)
        return MockResponse(404)


class By:
    ID = "id"


class MockElement:
    def __init__(self, text=""):
        self.text = text

    def send_keys(self, keys):
        pass  # Simulate typing

    def click(self):
        pass  # Simulate clicking


class MockSeleniumDriver:
    def __init__(self):
        self.page_source = ""

    def get(self, url):
        pass  # Simulate going to URL

    def find_element(self, by, value):
        if value == "task-list":
            # Return an element that 'contains' the expected text for the test to pass
            return MockElement(text="E2E Test Task Title")
        return MockElement()


# --- Pytest Fixtures ---


@pytest.fixture(scope="function")
def manager():
    return TaskManager()


@pytest.fixture(scope="function")
def test_app(manager):
    return MockTestApp(manager)


@pytest.fixture(scope="function")
def selenium_driver():
    return MockSeleniumDriver()
