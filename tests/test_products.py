from grocery_portal.db import get_db


def get_product_by_name(app, name):
    with app.app_context():
        db = get_db()

        return db.execute(
            """
            SELECT
                id,
                name,
                description,
                image_path,
                price,
                stock_quantity,
                is_on_sale,
                sale_price
            FROM products
            WHERE name = ?
            """,
            (name,),
        ).fetchone()


def insert_product(
    app,
    *,
    name="Existing Product",
    description="Original description",
    image_path="images/products/original.png",
    price=4.99,
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
                image_path,
                price,
                stock_quantity,
                is_on_sale,
                sale_price,
            ),
        )

        db.commit()

        return cursor.lastrowid


def get_product_by_name(app, name):
    with app.app_context():
        db = get_db()

        return db.execute(
            """
            SELECT
                id,
                name,
                description,
                image_path,
                price,
                stock_quantity,
                is_on_sale,
                sale_price
            FROM products
            WHERE name = ?
            """,
            (name,),
        ).fetchone()


def insert_product(
    app,
    *,
    name="Existing Product",
    description="Original description",
    image_path="images/products/original.png",
    price=4.99,
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
                image_path,
                price,
                stock_quantity,
                is_on_sale,
                sale_price,
            ),
        )

        db.commit()

        return cursor.lastrowid


def test_create_product_uses_default_image_path(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Rice",
            "description": "Long grain rice",
            "image_path": "",
            "price": "3.25",
            "stock_quantity": "20",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    product = get_product_by_name(app, "Rice")

    assert product is not None
    assert product["image_path"] == "images/products/placeholder.png"


def test_create_sale_product_saves_sale_price(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Cereal",
            "description": "Breakfast cereal",
            "image_path": "images/products/cereal.jpg",
            "price": "5.00",
            "stock_quantity": "15",
            "is_on_sale": "on",
            "sale_price": "4.00",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Product created successfully." in response.data

    product = get_product_by_name(app, "Cereal")

    assert product is not None
    assert product["is_on_sale"] == 1
    assert float(product["sale_price"]) == 4.00


def test_create_product_rejects_missing_name(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "",
            "description": "Invalid product",
            "image_path": "",
            "price": "2.99",
            "stock_quantity": "5",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Product name is required." in response.data
    assert get_product_by_name(app, "") is None


def test_create_product_rejects_negative_price(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Invalid Price Product",
            "description": "Should not be saved",
            "image_path": "",
            "price": "-2.99",
            "stock_quantity": "5",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Price must be a valid non-negative number." in response.data

    assert get_product_by_name(app, "Invalid Price Product") is None


def test_create_product_rejects_nonnumeric_price(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Invalid Text Price",
            "description": "Should not be saved",
            "image_path": "",
            "price": "abc",
            "stock_quantity": "5",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Price must be a valid non-negative number." in response.data

    assert get_product_by_name(app, "Invalid Text Price") is None


def test_create_product_rejects_decimal_quantity(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Invalid Quantity Product",
            "description": "Should not be saved",
            "image_path": "",
            "price": "2.99",
            "stock_quantity": "5.5",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Quantity must be a valid whole number." in response.data

    assert get_product_by_name(app, "Invalid Quantity Product") is None


def test_create_product_rejects_negative_quantity(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Negative Quantity Product",
            "description": "Should not be saved",
            "image_path": "",
            "price": "2.99",
            "stock_quantity": "-1",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Quantity must be a valid whole number." in response.data

    assert get_product_by_name(app, "Negative Quantity Product") is None


def test_create_sale_product_requires_sale_price(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Missing Sale Price",
            "description": "Should not be saved",
            "image_path": "",
            "price": "5.00",
            "stock_quantity": "10",
            "is_on_sale": "on",
            "sale_price": "",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Sale price is required when a product is on sale." in response.data

    assert get_product_by_name(app, "Missing Sale Price") is None


def test_create_sale_product_requires_lower_sale_price(
    app,
    authenticated_client,
):
    response = authenticated_client.post(
        "/products/new",
        data={
            "name": "Invalid Sale Price",
            "description": "Should not be saved",
            "image_path": "",
            "price": "5.00",
            "stock_quantity": "10",
            "is_on_sale": "on",
            "sale_price": "5.00",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Sale price must be less than the regular price." in response.data

    assert get_product_by_name(app, "Invalid Sale Price") is None


def test_edit_product_updates_product(
    app,
    authenticated_client,
):
    product_id = insert_product(
        app,
        name="Orange Juice",
        description="Half gallon orange juice",
        image_path="images/products/orangejuice.jpg",
        price=4.99,
        stock_quantity=12,
    )

    response = authenticated_client.post(
        f"/products/{product_id}/edit",
        data={
            "name": "Orange Juice",
            "description": ("Half gallon pulp-free orange juice"),
            "image_path": "images/products/orangejuice.jpg",
            "price": "5.49",
            "stock_quantity": "8",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Product updated successfully." in response.data

    product = get_product_by_name(app, "Orange Juice")

    assert product is not None
    assert product["description"] == "Half gallon pulp-free orange juice"
    assert float(product["price"]) == 5.49
    assert product["stock_quantity"] == 8


def test_edit_product_can_enable_sale(
    app,
    authenticated_client,
):
    product_id = insert_product(
        app,
        name="Coffee",
        price=8.99,
        stock_quantity=20,
    )

    response = authenticated_client.post(
        f"/products/{product_id}/edit",
        data={
            "name": "Coffee",
            "description": "Medium roast coffee",
            "image_path": "images/products/coffee.jpg",
            "price": "8.99",
            "stock_quantity": "20",
            "is_on_sale": "on",
            "sale_price": "6.99",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Product updated successfully." in response.data

    product = get_product_by_name(app, "Coffee")

    assert product["is_on_sale"] == 1
    assert float(product["sale_price"]) == 6.99


def test_edit_product_can_remove_sale(
    app,
    authenticated_client,
):
    product_id = insert_product(
        app,
        name="Sale Coffee",
        price=8.99,
        stock_quantity=20,
        is_on_sale=1,
        sale_price=6.99,
    )

    response = authenticated_client.post(
        f"/products/{product_id}/edit",
        data={
            "name": "Sale Coffee",
            "description": "No longer on sale",
            "image_path": "images/products/coffee.jpg",
            "price": "8.99",
            "stock_quantity": "20",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200

    product = get_product_by_name(app, "Sale Coffee")

    assert product["is_on_sale"] == 0
    assert product["sale_price"] is None


def test_invalid_edit_does_not_change_product(
    app,
    authenticated_client,
):
    product_id = insert_product(
        app,
        name="Original Product",
        description="Original description",
        price=4.99,
        stock_quantity=10,
    )

    response = authenticated_client.post(
        f"/products/{product_id}/edit",
        data={
            "name": "Changed Product",
            "description": "Changed description",
            "image_path": "",
            "price": "-1.00",
            "stock_quantity": "7",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Price must be a valid non-negative number." in response.data

    original = get_product_by_name(app, "Original Product")
    changed = get_product_by_name(app, "Changed Product")

    assert original is not None
    assert original["description"] == "Original description"
    assert float(original["price"]) == 4.99
    assert original["stock_quantity"] == 10
    assert changed is None


def test_edit_nonexistent_product_redirects_to_catalog(
    authenticated_client,
):
    response = authenticated_client.get(
        "/products/999999/edit",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Product not found." in response.data
