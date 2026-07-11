# Exercise: Deleting Expenses

## Goal

Complete the TDD cycle to implement a `delete_expense` method.

Our expense tracker has Create and Read functionality, now let's add Delete!

Files to work with:

- `tests/test_tracker.py`
- `src/tracker.py`

## UUIDs

In order to locate a specific expense for deletion, each expense needs to have an identifier (ID). We have already implemented this using Python's built-in `uuid` module.

## Instructions

### Step 1 - Review the Existing Code

The provided code has some more advanced techniques that you may not have encountered before.

`test_tracker.py` uses a pytest **fixture** to avoid repetitive setup code. You do not need to understand fully how this works, but read through the code to see how the `tracker` variable is passed in as an argument to our tests.

`tracker.py` uses the Python `@property` decorator. This allows us to calculate a `total` value whenever this attribute is requested. To external code, the `total` method is indistinguishable from a regular attribute of an `ExpenseTracker` instance.

### Step 2 - Red: Write the Test for Deletion

In `test_tracker.py`, implement `test_delete_expense(tracker)`:
- The `tracker` has been created using the fixture, so you do not need to instantiate a new `tracker` object
- Add an expense and capture the ID
- Call `tracker.delete_expense(expense_id)`
- Assert `tracker.total` is updated to 0
- Assert `tracker.get_expense(expense_id)` returns `None`

### Step 3 - Green: Implement Deletion

In `tracker.py`, implement the `delete_expense` method. Use the simplest possible code to pass the test.

Note that you do not need to change any logic in order to retrieve the `total`. If an expense has been removed from the `expenses` list, its amount will automatically be deducted from the total.

### (Optional) Step 4 - Refactor

Think about edge cases, such as attempting to delete a non-existent expense. Should this produce an error? Should it return `None`? Guide your (optional) refactor with tests.
