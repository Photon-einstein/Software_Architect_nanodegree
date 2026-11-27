# Project Rubric

Use this project rubric to understand and assess the project criteria.

## Design Pattern Implementation

| Criteria | Submission Requirements |
| --- | --- |
| **Singleton Pattern for Balance Management** | A `Singleton` balance class is implemented correctly to ensure only one instance of the balance exists across the application. |
| **Adapter Pattern for External Transactions** | An `ExternalFreelanceIncome` class and `TransactionAdapter` are included. The adapter correctly converts external data to internal `Transaction` objects. |
| **Observer Pattern for Low Balance Alerts and Balance Changes** | A `LowBalanceAlertObserver` class is implemented and registered with the `Balance` class. An alert is triggered when the balance falls below a defined threshold. Additionally, a `PrintBalance` class is implemented and registered with the `Balance` class. The balance is printed when a new transaction is applied. |
| **Fourth Design Pattern (Student's Choice)** | The student selects and implements one additional design pattern that has not already been used and documents the use clearly. |

## Industry Best Practices

| Criteria | Submission Requirements |
| --- | --- |
| **Effective Unit Testing** | Unit tests are written for `Balance`, `Transaction`, the adapter, observers, and the custom pattern. Tests run without errors. |
| **Successful Project Execution and Transaction Processing** | Running `main.py` simulates processing transactions and reflects the updated balance and alerts. |
| **Clean, Modular, and Pythonic Code** | Code follows PEP 8 standards, uses idiomatic Python, and organizes classes by file and function. No large functions or excessive duplication are present. |

## Reflection

| Criteria | Submission Requirements |
| --- | --- |
| **Reflection and Pattern Rationale** | A short written reflection is included that explains the four patterns used, why each was chosen, and any trade-offs or challenges encountered. |

## Suggestions to Make Your Project Stand Out

- **Add Undo/Redo Capability with the Command Pattern:** Implement command objects for applying transactions and allow users to undo the last transaction.
- **Add a Strategy for Budget Planning:** Let users choose between budgeting strategies, such as the **50/30/20 Rule** or **Zero-Based Budgeting**, and apply those strategies dynamically.
- **Introduce Transaction Validation or Logging with a Decorator:** Use a decorator to log each transaction or validate inputs before applying them to the balance.
