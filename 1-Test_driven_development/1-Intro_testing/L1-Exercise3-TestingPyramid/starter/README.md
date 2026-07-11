# Exercise: Building the Test Pyramid Layers

For this exercise, we will use our **Task Manager** application again to illustrate the *scope* of each test type, making the differences crystal clear. We'll simulate a simple web application scenario with a three-layer structure:

1.  **Logic Layer** (the `TaskManager` class, our Unit).
2.  **API Layer** (a Flask endpoint that uses the `TaskManager`, our Integration Point).
3.  **User Layer** (a simulation of a user interacting with the whole system, our E2E).

## Instructions

Your goal is to complete the three incomplete test functions to demonstrate the three layers of the pyramid.

## Code Structure and Dependencies

  * `src/task_manager.py` (Your main application code)
  * `tests/test_pyramid.py` (Where you will write the three tests)

For this exercise, assume we have the following tools available:

  * A fully implemented `TaskManager` class.
  * A `test_app` fixture (simulating an API client) that interacts with a Flask endpoint: `/api/task`.
  * A `selenium_driver` fixture (simulating a web browser) that interacts with a live URL: `http://localhost:8000/`.

## The Three Tests to Complete

### 1. Unit Test (The Foundation)

**Focus:** Testing the internal logic of a single function, isolated from the world.

### 2. Integration Test (The Plumbing)

**Focus:** Testing the connection between the web API layer and the core logic/database layer. It asks, "Can we successfully create a task via the API?"

### 3. End-to-End Test (The Final Walkthrough)

**Focus:** Simulating a user's entire journey, starting and ending at the UI.

---

Now, take a few minutes to fill in the `TODO` lines to demonstrate each level of the pyramid!
