# API Documentation

The Order Tracker API provides endpoints for creating, retrieving, updating, and listing customer orders.

## Base URL

```
http://localhost:5000
```

---

## Create an Order

**POST** `/api/orders`

Creates a new order.

### Request Body

```json
{
  "order_id": "ORD001",
  "item_name": "Laptop",
  "quantity": 2,
  "customer_id": "CUST100",
  "status": "pending"
}
```

### Success Response

**201 Created**

```json
{
  "order_id": "ORD001",
  "item_name": "Laptop",
  "quantity": 2,
  "customer_id": "CUST100",
  "status": "pending"
}
```

### Example

```bash
curl -X POST http://localhost:5000/api/orders \
-H "Content-Type: application/json" \
-d '{
  "order_id":"ORD001",
  "item_name":"Laptop",
  "quantity":2,
  "customer_id":"CUST100",
  "status":"pending"
}'
```

---

## Get an Order

**GET** `/api/orders/{order_id}`

Retrieves an order by its ID.

### Example

```bash
curl http://localhost:5000/api/orders/ORD001
```

### Success Response

```json
{
  "order_id": "ORD001",
  "item_name": "Laptop",
  "quantity": 2,
  "customer_id": "CUST100",
  "status": "pending"
}
```

---

## Update Order Status

**PUT** `/api/orders/{order_id}/status`

Updates the status of an existing order.

### Request Body

```json
{
  "new_status": "processing"
}
```

### Example

```bash
curl -X PUT http://localhost:5000/api/orders/ORD001/status \
-H "Content-Type: application/json" \
-d '{
  "new_status":"processing"
}'
```

### Success Response

```json
{
  "order_id": "ORD001",
  "item_name": "Laptop",
  "quantity": 2,
  "customer_id": "CUST100",
  "status": "processing"
}
```

---

## List Orders

**GET** `/api/orders`

Returns all orders.

### Example

```bash
curl http://localhost:5000/api/orders
```

### Success Response

```json
[
  {
    "order_id": "ORD001",
    "item_name": "Laptop",
    "quantity": 2,
    "customer_id": "CUST100",
    "status": "processing"
  }
]
```

---

## Filter Orders by Status

**GET** `/api/orders?status=pending`

Returns only orders matching the supplied status.

### Example

```bash
curl "http://localhost:5000/api/orders?status=pending"
```

### Success Response

```json
[
  {
    "order_id": "ORD002",
    "item_name": "Mouse",
    "quantity": 1,
    "customer_id": "CUST101",
    "status": "pending"
  }
]
```

---

## Error Responses

| Status Code | Description                                  |
| ----------- | -------------------------------------------- |
| **400**     | Invalid request data or invalid order status |
| **404**     | Order not found                              |
| **409**     | Duplicate order ID                           |
