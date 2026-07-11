# Exercise: Expense Tracker Categories

Your current ExpenseTracker allows adding an amount but doesn't track what the expense was for. Your task is to start implementing a new feature: adding an expense category.

According to TDD, we must start by writing a test that clearly defines this new requirement and fails immediately.

##  Goal

Write a new test function that asserts an expense can be stored with a category. The test should fail when run.

Files to Work With

- `tests/test_tracker.py` (The file you will edit)
- `src/tracker.py` (The existing application code—DO NOT EDIT IT YET)

## The Feature to Test

The ExpenseTracker class currently has the method signature: `add_expense(self, amount)`

You need to write a test that expects the new method signature to accept a category argument: `add_expense(self, amount, category)`

## Instructions

### Step 1: Red - Add Expense with Category

In `tests/test_tracker.py`, write a new test function called `test_add_expense_can_store_category`. The test should assert the following behavior:

- Add an expense, supplying both an amount and a category string (e.g., "food").
- Assert that the expense data stored internally in the tracker contains this category string. (You'll need to know where your application stores its expense records, likely a `self.expenses` list or dictionary).

When you run `pytest` after writing this test, it should fail with a `TypeError` because your test calls `add_expense` with an extra argument (`category`), but the implementation in `src/tracker.py` isn't ready for it yet.

### Step 2: Green - Add Expense with Category

Make that test pass with the simplest code possible in `src/tracker.py`.

### Step 3: Red - Filter Expenses by Category

Back in `tests/test_tracker.py`, define a new test called `test_list_expenses_by_category_returns_only_requested_category`. The test should assert the following behavior:

- A method on the `ExpenseTracker` called `list_expenses_by_category` exists.
- This method accepts a string argument for the category, and retuns a list of expense records whose category string matches the string that was passed in.
- Assert that if you add multiple expenses to the tracker with different categories (e.g. "food" then "travel" then "food"), then you call this method, you only get the matching expense records, not all expense records. (Hint: loop over the list and check that each one has the right `category` value.)

When you run `pytest`, this should fail (likely with an `AttributeError`) because the method doesn't exist yet.

### Step 4: Green - Filter Expenses by Category

In `src/tracker.py`, implement the code to make the new test pass.

Run `pytest` again and confirm your new test (and previous tests) pass.

### Step 5 (Optional): Refactor

- If you duplicated logic while adding category support, clean it up now.
- Consider input validation (e.g., non-empty category strings).
- Keep behavior the same so all tests stay green.
