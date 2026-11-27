# Project Instructions

You will start with a provided skeleton codebase and implement core components using
classic object-oriented design patterns. The project requires you to apply three
required patterns and one additional pattern of your choice. Each pattern must be
implemented in Python and integrated into the working finance manager application.

## Required Steps

1. Implement a Singleton Balance class (Done)
   Ensure only one instance of the balance manager exists across the application using the Singleton pattern.

2. Complete the Transaction class (Done)
   Finish the Transaction class using an enum to represent the transaction type (INCOME, EXPENSE).

3. Implement the Adapter pattern (Done)
   Complete a TransactionAdapter class that converts external freelance income (with invoice ID and
   project details) into a compatible Transaction object.

4. Implement the Observer pattern (Done)
   Create and register a LowBalanceAlertObserver that gets notified and triggers an alert when the user’s balance falls below a defined threshold and PrintBalance Observer that gets triggered when there is a change in the balance.

5. Choose and Implement One Additional Pattern (Student’s Choice)
   You will select one additional design pattern to implement from the course curriculum:

## Students must document:

- Why they chose this pattern
- Where it fits into the app
- How it improves flexibility, testability, or scalability 6. Write Unit Tests
- Create unit tests for the Balance, Transaction, Adapter, Observer, and any custom pattern implementation.

7. Run and Demonstrate the Application
   Use the provided main.py script to simulate the app.

8. Reflect and Document
   Include a short reflection explaining:

- The four design patterns used
- How each improved the design
- Any trade-offs encountered during implementation
- Submission Instructions
