import pytest
from unittest.mock import Mock
from ..order_tracker import OrderTracker

# --- Fixtures for Unit Tests ---


@pytest.fixture
def mock_storage():
    """
    Provides a mock storage object for tests.
    This mock will be configured to simulate various storage behaviors.
    """
    mock = Mock()
    # By default, mock get_order to return None (no order found)
    mock.get_order.return_value = None
    # By default, mock get_all_orders to return an empty dict
    mock.get_all_orders.return_value = {}
    return mock


@pytest.fixture
def order_tracker(mock_storage):
    """
    Provides an OrderTracker instance initialized with the mock_storage.
    """
    return OrderTracker(mock_storage)


#
# --- Cycle 1: Adding a Basic Order ---
#


def test_add_order_successfully(order_tracker, mock_storage):
    """Tests adding a new order with default 'pending' status."""
    result = order_tracker.add_order("ORD001", "Laptop", 1, "CUST001")

    # We expect save_order to be called once
    mock_storage.save_order.assert_called_once()

    saved_order_id, saved_order = mock_storage.save_order.call_args[0]
    assert saved_order_id == "ORD001"
    assert saved_order["order_id"] == "ORD001"
    assert saved_order["item_name"] == "Laptop"
    assert saved_order["quantity"] == 1
    assert saved_order["customer_id"] == "CUST001"
    assert saved_order["status"] == "pending"

    # Confirm the method's return value matches what was saved
    assert result["order_id"] == "ORD001"
    assert result["item_name"] == "Laptop"
    assert result["quantity"] == 1
    assert result["customer_id"] == "CUST001"
    assert result["status"] == "pending"


def test_add_order_raises_error_if_exists(order_tracker, mock_storage):
    """Tests that adding an order with a duplicate ID raises a ValueError."""
    # Simulate that the storage finds an existing order
    mock_storage.get_order.return_value = {"order_id": "ORD_EXISTING"}

    with pytest.raises(
        ValueError, match="Order with ID 'ORD_EXISTING' already exists."
    ):
        order_tracker.add_order("ORD_EXISTING", "New Item", 1, "CUST001")


def test_add_order_raises_error_for_zero_quantity(order_tracker, mock_storage):
    """Tests that a quantity of zero raises a ValueError."""
    with pytest.raises(ValueError, match="Quantity must be a positive integer."):
        order_tracker.add_order("ORD012", "Lamp", 0, "CUST012")


def test_add_order_raises_error_for_negative_quantity(order_tracker, mock_storage):
    """Tests that a negative quantity raises a ValueError."""
    with pytest.raises(ValueError, match="Quantity must be a positive integer."):
        order_tracker.add_order("ORD013", "Lamp", -3, "CUST013")


def test_add_order_raises_error_for_missing_order_id(order_tracker, mock_storage):
    """Tests that an empty order_id raises a ValueError."""
    with pytest.raises(ValueError, match="order_id is required."):
        order_tracker.add_order("", "Lamp", 1, "CUST014")


def test_add_order_raises_error_for_missing_item_name(order_tracker, mock_storage):
    """Tests that an empty item_name raises a ValueError."""
    with pytest.raises(ValueError, match="item_name is required."):
        order_tracker.add_order("ORD015", "", 1, "CUST015")


def test_add_order_raises_error_for_missing_customer_id(order_tracker, mock_storage):
    """Tests that an empty customer_id raises a ValueError."""
    with pytest.raises(ValueError, match="customer_id is required."):
        order_tracker.add_order("ORD016", "Lamp", 1, "")


def test_add_order_raises_error_for_invalid_status(order_tracker, mock_storage):
    """Tests that a status outside the allowed set raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid status: 'unknown'."):
        order_tracker.add_order("ORD017", "Lamp", 1, "CUST017", status="unknown")


def test_add_order_validates_input_before_checking_storage(order_tracker, mock_storage):
    """Tests that invalid input is rejected without ever reading from storage (fail fast)."""
    with pytest.raises(ValueError):
        order_tracker.add_order("ORD018", "Lamp", 0, "CUST018")

    mock_storage.get_order.assert_not_called()


#
# --- Cycle 2: Fetching an Order by ID ---
#


def test_get_order_by_id_success(order_tracker, mock_storage):
    """Tests fetching an existing order returns the correct order data."""
    expected_order = {
        "order_id": "ORD002",
        "item_name": "Mouse",
        "quantity": 2,
        "customer_id": "CUST002",
        "status": "pending",
    }
    mock_storage.get_order.return_value = expected_order

    result = order_tracker.get_order_by_id("ORD002")

    mock_storage.get_order.assert_called_once_with("ORD002")
    assert result == expected_order


def test_get_order_by_id_returns_none_if_not_found(order_tracker):
    """Tests that fetching a non-existent order returns None (not an exception)."""
    result = order_tracker.get_order_by_id("MISSING001")
    assert result is None


def test_get_order_by_id_raises_error_for_empty_id(order_tracker):
    """Tests that an empty order_id raises a ValueError."""
    with pytest.raises(ValueError, match="order_id is required."):
        order_tracker.get_order_by_id("")


#
# --- Cycle 3: Updating an Order's Status ---
#


def test_update_order_status_raises_error_for_invalid_status(
    order_tracker, mock_storage
):
    """Tests that a status outside the allowed set raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid status: 'unknown'."):
        order_tracker.update_order_status("ORD004", "unknown")


def test_update_order_status_raises_error_for_empty_id(order_tracker, mock_storage):
    """Tests that an empty order_id raises a ValueError."""
    with pytest.raises(ValueError, match="order_id is required."):
        order_tracker.update_order_status("", "shipped")


def test_update_order_status_validates_status_before_checking_storage(
    order_tracker, mock_storage
):
    """Tests that an invalid status is rejected without ever reading from storage (fail fast)."""
    with pytest.raises(ValueError):
        order_tracker.update_order_status("ORD005", "unknown")

    mock_storage.get_order.assert_not_called()


def test_update_order_status_success(order_tracker, mock_storage):
    """Tests that updating an existing order's status saves the change."""
    existing_order = {
        "order_id": "ORD003",
        "item_name": "Keyboard",
        "quantity": 1,
        "customer_id": "CUST003",
        "status": "pending",
    }
    mock_storage.get_order.return_value = existing_order

    result = order_tracker.update_order_status("ORD003", "shipped")

    mock_storage.save_order.assert_called_once()
    saved_order_id, saved_order = mock_storage.save_order.call_args[0]
    assert saved_order_id == "ORD003"
    assert saved_order["status"] == "shipped"
    assert result["status"] == "shipped"


def test_update_order_status_raises_error_if_not_found(order_tracker, mock_storage):
    """Tests that updating a non-existent order raises a ValueError."""
    with pytest.raises(ValueError, match="Order with ID 'MISSING002' not found."):
        order_tracker.update_order_status("MISSING002", "shipped")


#
# --- Cycle 4: Listing All Orders ---
#


def test_list_all_orders_returns_all(order_tracker, mock_storage):
    """Tests that all stored orders are returned as a list."""
    mock_storage.get_all_orders.return_value = {
        "ORD004": {
            "order_id": "ORD004",
            "item_name": "Monitor",
            "quantity": 1,
            "customer_id": "CUST004",
            "status": "pending",
        },
        "ORD005": {
            "order_id": "ORD005",
            "item_name": "Webcam",
            "quantity": 1,
            "customer_id": "CUST005",
            "status": "shipped",
        },
    }

    result = order_tracker.list_all_orders()

    assert len(result) == 2
    assert {order["order_id"] for order in result} == {"ORD004", "ORD005"}


def test_list_all_orders_returns_empty_list_when_no_orders(order_tracker, mock_storage):
    """Tests that an empty list is returned when there are no orders."""
    # mock_storage.get_all_orders already defaults to returning {}
    result = order_tracker.list_all_orders()

    assert result == []


#
# --- Cycle 5: Listing Orders By Status ---
#


def test_list_orders_by_status_returns_matching_orders(order_tracker, mock_storage):
    """Tests that only orders matching the given status are returned."""
    mock_storage.get_all_orders.return_value = {
        "ORD006": {
            "order_id": "ORD006",
            "item_name": "Desk",
            "quantity": 1,
            "customer_id": "CUST006",
            "status": "pending",
        },
        "ORD007": {
            "order_id": "ORD007",
            "item_name": "Chair",
            "quantity": 1,
            "customer_id": "CUST007",
            "status": "shipped",
        },
    }

    result = order_tracker.list_orders_by_status("shipped")

    assert len(result) == 1
    assert result[0]["order_id"] == "ORD007"


def test_list_orders_by_status_returns_empty_list_when_no_matches(
    order_tracker, mock_storage
):
    """Tests that an empty list is returned when no orders match the status."""
    mock_storage.get_all_orders.return_value = {
        "ORD008": {
            "order_id": "ORD008",
            "item_name": "Lamp",
            "quantity": 1,
            "customer_id": "CUST008",
            "status": "pending",
        },
    }

    result = order_tracker.list_orders_by_status("shipped")

    assert result == []


def test_list_orders_by_status_returns_empty_list_for_empty_storage(order_tracker):
    """Tests that an empty list is returned when storage has no orders at all."""
    result = order_tracker.list_orders_by_status("pending")
    assert result == []


def test_list_orders_by_status_raises_error_for_empty_status(order_tracker):
    """Tests that an empty status string raises a ValueError."""
    with pytest.raises(ValueError, match="status is required."):
        order_tracker.list_orders_by_status("")


def test_list_orders_by_status_raises_error_for_invalid_status(order_tracker):
    """Tests that a status outside the allowed set raises a ValueError."""
    with pytest.raises(ValueError, match="Invalid status: 'unknown'."):
        order_tracker.list_orders_by_status("unknown")
