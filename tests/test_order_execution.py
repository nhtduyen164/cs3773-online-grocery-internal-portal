from grocery_portal.db import get_db


def insert_product(
    app,
    *,
    name,
    stock_quantity,
    price=5.00,
):
    """
    Insert a product and return its generated ID.
    """

    with app.app_context():
        db = get_db()

        cursor = db.execute(
            """
            INSERT INTO products (
                name,
                description,
                image_path,
                price,
                stock_quantity,
                is_on_sale,
                sale_price
            )
            VALUES (?, ?, ?, ?, ?, 0, NULL)
            """,
            (
                name,
                f"Test product: {name}",
                "images/products/placeholder.png",
                price,
                stock_quantity,
            ),
        )

        db.commit()

        return cursor.lastrowid


def insert_order(
    app,
    *,
    customer_name="Test Customer",
    status="placed",
    subtotal=10.00,
    discount_amount=0.00,
    total_amount=10.00,
):
    """
    Insert an order and return its generated ID.
    """

    with app.app_context():
        db = get_db()

        cursor = db.execute(
            """
            INSERT INTO orders (
                customer_name,
                status,
                subtotal,
                discount_amount,
                total_amount
            )
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                customer_name,
                status,
                subtotal,
                discount_amount,
                total_amount,
            ),
        )

        db.commit()

        return cursor.lastrowid


def insert_order_item(
    app,
    *,
    order_id,
    product_id,
    quantity,
    unit_price=5.00,
):
    """
    Add one product to an order.
    """

    with app.app_context():
        db = get_db()

        db.execute(
            """
            INSERT INTO order_items (
                order_id,
                product_id,
                quantity,
                unit_price
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                order_id,
                product_id,
                quantity,
                unit_price,
            ),
        )

        db.commit()


def get_product_stock(app, product_id):
    """
    Return the current stock quantity for a product.
    """

    with app.app_context():
        db = get_db()

        product = db.execute(
            """
            SELECT stock_quantity
            FROM products
            WHERE id = ?
            """,
            (product_id,),
        ).fetchone()

        return product["stock_quantity"]


def get_order_status(app, order_id):
    """
    Return the current status of an order.
    """

    with app.app_context():
        db = get_db()

        order = db.execute(
            """
            SELECT status
            FROM orders
            WHERE id = ?
            """,
            (order_id,),
        ).fetchone()

        return order["status"]


def test_execute_order_reduces_inventory_and_completes_order(
    app,
    authenticated_client,
):
    first_product_id = insert_product(
        app,
        name="Test Apples",
        stock_quantity=20,
        price=2.00,
    )

    second_product_id = insert_product(
        app,
        name="Test Bread",
        stock_quantity=12,
        price=4.00,
    )

    order_id = insert_order(
        app,
        customer_name="Successful Customer",
        subtotal=12.00,
        total_amount=12.00,
    )

    insert_order_item(
        app,
        order_id=order_id,
        product_id=first_product_id,
        quantity=4,
        unit_price=2.00,
    )

    insert_order_item(
        app,
        order_id=order_id,
        product_id=second_product_id,
        quantity=1,
        unit_price=4.00,
    )

    response = authenticated_client.post(
        f"/orders/{order_id}/execute",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Order executed successfully." in response.data

    assert get_product_stock(app, first_product_id) == 16
    assert get_product_stock(app, second_product_id) == 11

    assert get_order_status(app, order_id) == "completed"


def test_execute_order_with_insufficient_inventory_changes_nothing(
    app,
    authenticated_client,
):
    available_product_id = insert_product(
        app,
        name="Available Product",
        stock_quantity=20,
    )

    short_product_id = insert_product(
        app,
        name="Short Product",
        stock_quantity=2,
    )

    order_id = insert_order(
        app,
        customer_name="Insufficient Inventory Customer",
    )

    insert_order_item(
        app,
        order_id=order_id,
        product_id=available_product_id,
        quantity=5,
    )

    insert_order_item(
        app,
        order_id=order_id,
        product_id=short_product_id,
        quantity=3,
    )

    response = authenticated_client.post(
        f"/orders/{order_id}/execute",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Not enough inventory to execute this order" in response.data
    assert b"Short Product" in response.data

    assert get_product_stock(app, available_product_id) == 20
    assert get_product_stock(app, short_product_id) == 2

    assert get_order_status(app, order_id) == "placed"


def test_completed_order_cannot_be_executed_again(
    app,
    authenticated_client,
):
    product_id = insert_product(
        app,
        name="Previously Purchased Product",
        stock_quantity=15,
    )

    order_id = insert_order(
        app,
        customer_name="Completed Order Customer",
        status="completed",
    )

    insert_order_item(
        app,
        order_id=order_id,
        product_id=product_id,
        quantity=4,
    )

    response = authenticated_client.post(
        f"/orders/{order_id}/execute",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Only currently placed orders can be executed." in response.data

    assert get_product_stock(app, product_id) == 15
    assert get_order_status(app, order_id) == "completed"


def test_order_without_items_cannot_be_executed(
    app,
    authenticated_client,
):
    order_id = insert_order(
        app,
        customer_name="Empty Order Customer",
    )

    response = authenticated_client.post(
        f"/orders/{order_id}/execute",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"This order does not contain any items." in response.data

    assert get_order_status(app, order_id) == "placed"


def test_execute_order_can_reduce_inventory_to_zero(
    app,
    authenticated_client,
):
    product_id = insert_product(
        app,
        name="Last Product in Stock",
        stock_quantity=5,
    )

    order_id = insert_order(
        app,
        customer_name="Exact Inventory Customer",
    )

    insert_order_item(
        app,
        order_id=order_id,
        product_id=product_id,
        quantity=5,
    )

    response = authenticated_client.post(
        f"/orders/{order_id}/execute",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Order executed successfully." in response.data

    assert get_product_stock(app, product_id) == 0
    assert get_order_status(app, order_id) == "completed"


def test_execute_order_requires_login(
    app,
    client,
):
    product_id = insert_product(
        app,
        name="Protected Product",
        stock_quantity=10,
    )

    order_id = insert_order(
        app,
        customer_name="Unauthenticated Customer",
    )

    insert_order_item(
        app,
        order_id=order_id,
        product_id=product_id,
        quantity=2,
    )

    response = client.post(
        f"/orders/{order_id}/execute",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]

    assert get_product_stock(app, product_id) == 10
    assert get_order_status(app, order_id) == "placed"


def test_execute_nonexistent_order_returns_404(
    authenticated_client,
):
    response = authenticated_client.post(
        "/orders/999999/execute",
    )

    assert response.status_code == 404



