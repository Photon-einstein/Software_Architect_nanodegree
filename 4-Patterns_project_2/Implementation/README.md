# Personal Finance Manager — Design Patterns Project

This project is a hands-on exercise in applying Object-Oriented Design Patterns to build a simplified personal finance manager.
You will implement and extend starter code to add functionality such as tracking transactions, adapting external data, observing balance changes, and ensuring proper architectural patterns.

## Getting Started

### Dependencies

Make sure you have python version >= 3.10.x installed on your computer.

### Installation

1. Clone the repo:

```
bash
git clone https://github.com/udacity/cd14600-project-starter.git
cd cd14600-project-starter/starter
```

2. Run the Program:

```
python main.py
```

## Testing

This project uses Python’s built-in unittest framework.

From the `Implementation` directory, run all tests:

```
python -m unittest discover
```

To run a single test file:

```
python -m unittest balance.test_balance_observer
python -m unittest transaction.test_transaction
python -m unittest transaction.test_transaction_adapter
python -m unittest transaction.test_transaction_command
```

### Break Down Tests

- test_balance.py → Verifies correct implementation of the Singleton Balance class.
- test_transaction.py → Confirms transactions update balances correctly.
- test_transaction_adapter.py → Ensures external income data is correctly adapted into Transaction objects.
- test_balance_observer.py → Validates that low-balance alerts are triggered at the correct threshold.
- test_transaction_command.py → Checks transaction commands and undo history.

## Design Pattern Reflection

- **Singleton:** `Balance` keeps a shared balance throughout the application. This
  simplifies access, but its shared state needs care in tests.
- **Adapter:** `TransactionAdapter` converts external freelance income into an
  internal transaction. This separates external data from balance processing;
  invoice details are not retained in the internal transaction.
- **Observer:** Balance observers print updates and low-balance alerts without
  coupling those behaviors to transaction processing.
- **Command:** `TransactionCommand` encapsulates applying and undoing a transaction,
  while `TransactionHistory` tracks commands in last-in, first-out order. This adds
  undo without changing balance arithmetic and makes commands independently testable.
  Undo applies an opposite transaction and notifies observers; history is in memory,
  covers only commands executed through it, and does not provide redo.

## Project Instructions

1. Implement Singleton Balance Class – Ensure only one balance object exists throughout the app.
2. Complete Transaction Class – Handle income and expense transactions.
3. Implement Adapter Pattern – Adapt external freelance income data into internal Transaction objects.
4. Implement Observer Pattern – Create a low balance observer that triggers an alert when funds drop too low.
5. Add Unit Tests – Write tests for all implemented functionality.
6. Choose and Implement a Fourth Pattern – Pick one additional design pattern (e.g., Strategy, Command, Decorator, etc.) and integrate it into your project.
7. Provide a Reflection – Add a short write-up in your repo (README or separate file) explaining your design choices.

## Built With

- [Python](https://www.python.org/) – Main programming language
- [unittest](https://docs.python.org/3/library/unittest.html) – Testing framework
- [PEP8](https://peps.python.org/pep-0008/) – Style guide for Python code
