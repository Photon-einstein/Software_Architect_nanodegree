# Personal Finance Manager

This folder contains the finance manager implementation and its tests.

## Design choices

- **Singleton:** `Balance` provides a shared balance to the application. This
  avoids conflicting balance instances, but shared state requires care when
  testing.
- **Adapter:** `TransactionAdapter` converts external freelance income into
  an internal `Transaction`, keeping external data separate from balance
  processing. The internal transaction does not retain the invoice ID or
  description.
- **Observer:** `PrintObserver` and `LowBalanceAlertObserver` respond to balance
  updates independently of the balance calculation. New observers can be added
  without changing that calculation, though notification is synchronous.
- **Command:** `TransactionCommand` encapsulates applying and reversing a
  transaction; `TransactionHistory` executes commands and undoes them in reverse
  order. This adds undo while reusing balance processing and notifications.
  History is kept in memory, tracks only commands executed through it, and
  does not support redo.
