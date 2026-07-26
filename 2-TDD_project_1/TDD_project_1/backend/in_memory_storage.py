class InMemoryStorage:
    """
    Simple in-memory storage implementation for orders.

    Orders are stored in a dictionary where the key is the
    order ID and the value is the order dictionary.

    This class is intended for development and testing purposes.
    All stored data is lost when the application stops.
    """

    def __init__(self):
        """
        Initializes an empty storage for orders.
        """
        self.orders = {}

    def save_order(self, order_id, order):
        """
        Stores or updates an order.

        If an order with the given ID already exists, it is
        overwritten with the new data.

        Args:
            order_id: Unique identifier of the order.
            order: Dictionary containing the order information.

        Returns:
            None
        """
        self.orders[order_id] = order

    def get_order(self, order_id):
        """
        Retrieves an order by its unique identifier.

        Args:
            order_id: ID of the order to retrieve.

        Returns:
            dict | None:
                The matching order if it exists; otherwise, None.
        """
        return self.orders.get(order_id)

    def get_all_orders(self):
        """
        Returns all stored orders.

        Returns:
            dict:
                A dictionary containing every stored order,
                keyed by order ID.
        """
        return self.orders
