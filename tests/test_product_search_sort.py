from grocery_portal.db import get_db


def insert_product(
    app,
    *,
    name,
    description="Test product",
    price=5.00,
    stock_quantity=10,
    is_on_sale=0,
    sale_price=None,
):
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
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                description,
                "images/products/placeholder.png",
                price,
                stock_quantity,
                is_on_sale,
                sale_price,
            ),
        )

        db.commit()
        return cursor.lastrowid


def test_search_product(
    app,
    authenticated_client,
):
    insert_product(app, name="Apple")
    insert_product(app, name="Orange")

    response = authenticated_client.get("/products?search=Apple")

    assert response.status_code == 200
    assert b"Apple" in response.data
    assert b"Orange" not in response.data


def test_search_no_results(
    app,
    authenticated_client,
):
    insert_product(app, name="Milk")

    response = authenticated_client.get("/products?search=Banana")

    assert response.status_code == 200
    assert b"Milk" not in response.data


def test_invalid_sort(
    app,
    authenticated_client,
):
    insert_product(app, name="Bananas")
    insert_product(app, name="Apples")

    response = authenticated_client.get("/products?sort=badsort")

    assert response.status_code == 200

    html = response.data.decode()

    assert html.index("Apples") < html.index("Bananas")


def test_sort_price_low_high(
    app,
    authenticated_client,
):
    insert_product(app, name="Cheap", price=1.00)
    insert_product(app, name="Expensive", price=10.00)

    response = authenticated_client.get("/products?sort=price_asc")

    assert response.status_code == 200

    html = response.data.decode()

    assert html.index("Cheap") < html.index("Expensive")


def test_sort_price_high_low(
    app,
    authenticated_client,
):
    insert_product(app, name="Cheap", price=1.00)
    insert_product(app, name="Expensive", price=10.00)

    response = authenticated_client.get("/products?sort=price_desc")

    assert response.status_code == 200

    html = response.data.decode()

    assert html.index("Expensive") < html.index("Cheap")


def test_sort_availability(
    app,
    authenticated_client,
):
    insert_product(app, name="Low", stock_quantity=2)
    insert_product(app, name="High", stock_quantity=100)

    response = authenticated_client.get("/products?sort=availability")

    assert response.status_code == 200
    assert b"Low" in response.data
    assert b"High" in response.data