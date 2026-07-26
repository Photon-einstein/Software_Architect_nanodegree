# This module contains the OrderTracker class, which encapsulates the core
# business logic for managing orders.


class InvalidOrderDataError(ValueError):
    """Raised when input data (fields, quantity, status) fails validation."""

    pass


class DuplicateOrderError(ValueError):
    """Raised when attempting to add an order with an ID that already exists."""

    pass


class OrderNotFoundError(ValueError):
    """Raised when an operation references an order_id that doesn't exist."""

    pass


class OrderTracker:
    """
    Encapsulates the business logic for managing customer orders.

    The OrderTracker is responsible for validating order data,
    interacting with the storage layer, and providing operations
    for creating, retrieving, updating, and listing orders.
    """

    VALID_STATUSES = {"pending", "processing", "shipped"}

    def __init__(self, storage):
        """
        Initializes the OrderTracker with a storage implementation.

        The provided storage object must implement the following methods:
        - save_order(order_id, order)
        - get_order(order_id)
        - get_all_orders()

        Raises:
            TypeError: If the storage object does not implement the
                required interface.
        """
        required_methods = ["save_order", "get_order", "get_all_orders"]

        for method in required_methods:
            if not hasattr(storage, method) or not callable(getattr(storage, method)):
                raise TypeError(
                    f"Storage object must implement a callable '{method}' method."
                )

        self.storage = storage

    def add_order(
        self,
        order_id: str,
        item_name: str,
        quantity: int,
        customer_id: str,
        status: str = "pending",
    ):
        """
        Creates and stores a new order.

        All input values are validated before interacting with the
        storage layer. If an order with the same ID already exists,
        an exception is raised.

        Args:
            order_id: Unique identifier for the order.
            item_name: Name of the ordered item.
            quantity: Number of items ordered.
            customer_id: Identifier of the customer.
            status: Initial order status (defaults to "pending").

        Returns:
            dict: The newly created order.

        Raises:
            InvalidOrderDataError:
                If any field is missing or invalid.
            DuplicateOrderError:
                If an order with the same ID already exists.
        """
        # Validate required fields first (fail fast)
        if not order_id:
            raise InvalidOrderDataError("order_id is required.")
        if not item_name:
            raise InvalidOrderDataError("item_name is required.")
        if not customer_id:
            raise InvalidOrderDataError("customer_id is required.")
        if not isinstance(quantity, int) or quantity <= 0:
            raise InvalidOrderDataError("Quantity must be a positive integer.")
        if status not in self.VALID_STATUSES:
            raise InvalidOrderDataError(f"Invalid status: '{status}'.")

        # Only access storage after validation succeeds
        if self.storage.get_order(order_id):
            raise DuplicateOrderError(f"Order with ID '{order_id}' already exists.")

        order = {
            "order_id": order_id,
            "item_name": item_name,
            "quantity": quantity,
            "customer_id": customer_id,
            "status": status,
        }

        self.storage.save_order(order_id, order)
        return order

    def get_order_by_id(self, order_id: str):
        """
        Retrieves an order using its unique identifier.

        Args:
            order_id: The ID of the order to retrieve.

        Returns:
            dict | None:
                The matching order if found, otherwise None.

        Raises:
            InvalidOrderDataError:
                If the order ID is empty.
        """
        if not order_id:
            raise InvalidOrderDataError("order_id is required.")

        return self.storage.get_order(order_id)

    def update_order_status(self, order_id: str, new_status: str):
        """
        Updates the status of an existing order.

        The order must exist, and the new status must be one of the
        supported values.

        Args:
            order_id: ID of the order to update.
            new_status: The new order status.

        Returns:
            dict: The updated order.

        Raises:
            InvalidOrderDataError:
                If the order ID or status is invalid.
            OrderNotFoundError:
                If the order does not exist.
        """
        if not order_id:
            raise InvalidOrderDataError("order_id is required.")

        if new_status not in self.VALID_STATUSES:
            raise InvalidOrderDataError(f"Invalid status: '{new_status}'.")

        order = self.storage.get_order(order_id)

        if order is None:
            raise OrderNotFoundError(f"Order with ID '{order_id}' not found.")

        order["status"] = new_status
        self.storage.save_order(order_id, order)

        return order

    def list_all_orders(self):
        """
        Returns every stored order.

        Returns:
            list[dict]:
                A list containing all stored orders.
        """
        return list(self.storage.get_all_orders().values())

    def list_orders_by_status(self, status: str):
        """
        Returns all orders matching a specific status.

        Args:
            status: The status used to filter orders.

        Returns:
            list[dict]:
                A list of orders whose status matches the supplied value.

        Raises:
            InvalidOrderDataError:
                If the status is empty or invalid.
        """
        if not status:
            raise InvalidOrderDataError("status is required.")

        if status not in self.VALID_STATUSES:
            raise InvalidOrderDataError(f"Invalid status: '{status}'.")

        results = self.list_all_orders()

        return [result for result in results if result["status"] == status]
