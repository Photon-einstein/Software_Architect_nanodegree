#  Exercise: Red, Green, Refactor with a Task Manager

This exercise focuses on strictly applying the **Test-Driven Development (TDD)** cycle to implement a new feature for a `TaskManager` class. Your three steps are **Red**, **Green**, and **Refactor**.

## New Feature: Retrieve an Existing Task

You need to add a method to a `TaskManager` class called `get_task()`. This method must accept a unique task ID and return the corresponding task object.

## Initial Setup

For this exercise, assume the following starter code in two files:

1. `src/task_manager.py` (The App Code - Needs a New Method)
2. `tests/test_task_manager.py` (The Test Code)

## Instructions: Follow the TDD Cycle

### Phase 1: Red (Write the Failing Test)

1.  In **`tests/test_task_manager.py`**, add a new test function: `test_get_task_by_id()`.
2.  Inside this test, perform the necessary steps:
      * **Arrange**: Use the `manager` fixture to call `add_task()` and capture the returned `task_id`.
      * **Act**: Call the non-existent method, e.g., `retrieved_task = manager.get_task(task_id)`.
      * **Assert**: Assert that the `retrieved_task`'s `title` matches the title you initially created.
3.  Run `pytest`. It **must fail** with an `AttributeError` (or similar error) because the `get_task` method hasn't been implemented yet. You are now officially **Red**.

### Phase 2: Green (Write Minimal Code to Pass)

1.  Open the application file, **`src/task_manager.py`**.
2.  Implement the `get_task(self, task_id: str)` method in the `TaskManager` class.
3.  Write the **absolute minimum code** necessary to pass the new test you just wrote. This means accessing the task dictionary and returning the object.
4.  Run `pytest`. All tests must now pass (Green).

### Phase 3: Refactor (Make the Code Right)

1.  Look at the method you just implemented to pass the test. Does it handle edge cases? What happens if a user passes an ID that **doesn't exist**? The current method would likely raise a `KeyError`.
2.  **Refactor** the `get_task` method to handle the failure case gracefully by returning `None` (or raising a custom exception, but returning `None` is simpler for this intro).
3.  Now, go back to **`tests/test_task_manager.py`** and write a *new, simple test* to ensure your refactoring works: `test_get_task_nonexistent_returns_none()`. This proves your refactored code is more robust.
4.  Run `pytest` one last time. All tests should remain **Green**, confirming the refactoring was safe and improved the code quality.
