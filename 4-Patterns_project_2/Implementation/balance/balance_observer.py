# balance_observer.py


class IBalanceObserver:
    def update(self, balance, transaction):
        """Handle balance updates; transaction is None for direct changes."""
        raise NotImplementedError("Subclasses must implement update method.")


class PrintObserver(IBalanceObserver):
    def update(self, balance, transaction):
        """Print balance update message."""
        if transaction is not None:
            print(f"{transaction.category.value}: ${transaction.amount}")
        print(f"Balance updated: ${balance}")


class LowBalanceAlertObserver(IBalanceObserver):

    def __init__(self, threshold):
        self.threshold = threshold
        self.alert_triggered = False

    def update(self, balance, transaction):
        """Alert if balance drops below threshold."""
        self.alert_triggered = balance < self.threshold
        if self.alert_triggered:
            print(f"Low balance alert: ${balance} is below ${self.threshold}")
