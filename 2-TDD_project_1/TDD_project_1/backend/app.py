from flask import Flask, request, jsonify, send_from_directory
from backend.order_tracker import (
    OrderTracker,
    InvalidOrderDataError,
    DuplicateOrderError,
    OrderNotFoundError,
)
from backend.in_memory_storage import InMemoryStorage

# Create the Flask application and point it to the frontend folder
app = Flask(__name__, static_folder="../frontend")

# Initialize the storage and business logic objects
in_memory_storage = InMemoryStorage()
order_tracker = OrderTracker(in_memory_storage)


@app.route("/")
def serve_index():
    """
    Serves the main frontend page (index.html) when the root URL is accessed.
    """
    return send_from_directory(app.static_folder, "index.html")


@app.route("/<path:filename>")
def serve_static(filename):
    """
    Serves static frontend files such as JavaScript, CSS, or images.
    """
    return send_from_directory(app.static_folder, filename)


@app.route("/api/orders", methods=["POST"])
def add_order_api():
    """
    Creates a new order.

    Expects a JSON request containing:
    - order_id
    - item_name
    - quantity
    - customer_id
    - status (optional, defaults to 'pending')

    Returns:
    - 201 if the order is successfully created.
    - 400 if the provided data is invalid.
    - 409 if an order with the same ID already exists.
    """
    data = request.get_json()

    try:
        order = order_tracker.add_order(
            data["order_id"],
            data["item_name"],
            data["quantity"],
            data["customer_id"],
            data.get("status", "pending"),
        )
        return jsonify(order), 201

    except DuplicateOrderError as e:
        return jsonify({"error": str(e)}), 409

    except InvalidOrderDataError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/orders/<string:order_id>", methods=["GET"])
def get_order_api(order_id):
    """
    Retrieves an order by its ID.

    Returns:
    - 200 with the order if found.
    - 404 if no order exists with the given ID.
    """
    order = order_tracker.get_order_by_id(order_id)

    if order is None:
        return jsonify({"error": f"Order with ID '{order_id}' not found."}), 404

    return jsonify(order), 200


@app.route("/api/orders/<string:order_id>/status", methods=["PUT"])
def update_order_status_api(order_id):
    """
    Updates the status of an existing order.

    Expects a JSON body containing:
    - new_status

    Returns:
    - 200 if the status was successfully updated.
    - 400 if the new status is invalid.
    - 404 if the order cannot be found.
    """
    data = request.get_json()

    try:
        order = order_tracker.update_order_status(order_id, data["new_status"])
        return jsonify(order), 200

    except OrderNotFoundError as e:
        return jsonify({"error": str(e)}), 404

    except InvalidOrderDataError as e:
        return jsonify({"error": str(e)}), 400


@app.route("/api/orders", methods=["GET"])
def list_orders_api():
    """
    Returns all orders.

    Optional query parameter:
    - status

    If a status is provided, only orders matching that status are returned.
    Otherwise, all orders are returned.

    Returns:
    - 200 with the list of orders.
    - 400 if an invalid status filter is supplied.
    """
    status = request.args.get("status")

    if status:
        try:
            orders = order_tracker.list_orders_by_status(status)
        except ValueError as e:
            return jsonify({"error": str(e)}), 400
    else:
        orders = order_tracker.list_all_orders()

    return jsonify(orders), 200


if __name__ == "__main__":
    # Starts the Flask development server.
    # debug=True automatically reloads the server after code changes
    # and provides detailed error messages during development.
    app.run(host="0.0.0.0", debug=True)
