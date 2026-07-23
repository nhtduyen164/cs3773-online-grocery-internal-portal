from werkzeug.security import generate_password_hash

from grocery_portal.db import get_db
import pytest


def insert_user(
    app,
    *,
    username="employee1",
    password="password123",
    email="employee1@example.com",
    role="cashier",
):
    with app.app_context():
        db = get_db()

        cursor = db.execute(
            """
            INSERT INTO users (
                username,
                email,
                password_hash,
                role
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                username,
                email,
                generate_password_hash(password),
                role,
            ),
        )

        db.commit()

        return cursor.lastrowid


def test_login_page_loads(client):
    response = client.get("/login")

    assert response.status_code == 200
    assert b"password" in response.data.lower()


def test_valid_login_redirects_to_dashboard(
    app,
    client,
):
    user_id = insert_user(
        app,
        username="employee1",
        password="password123",
        role="cashier",
    )

    response = client.post(
        "/login",
        data={
            "username": "employee1",
            "password": "password123",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Login successful." in response.data

    with client.session_transaction() as session:
        assert session["user_id"] == user_id
        assert session["username"] == "employee1"
        assert session["role"] == "cashier"


def test_valid_login_redirects_to_dashboard_url(
    app,
    client,
):
    insert_user(
        app,
        username="employee1",
        password="password123",
    )

    response = client.post(
        "/login",
        data={
            "username": "employee1",
            "password": "password123",
        },
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/dashboard" in response.headers["Location"]


def test_invalid_password_does_not_log_user_in(
    app,
    client,
):
    insert_user(
        app,
        username="employee1",
        password="password123",
    )

    response = client.post(
        "/login",
        data={
            "username": "employee1",
            "password": "password1234",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Invalid username or password." in response.data

    with client.session_transaction() as session:
        assert "user_id" not in session
        assert "username" not in session
        assert "role" not in session


def test_unknown_username_does_not_log_user_in(
    client,
):
    response = client.post(
        "/login",
        data={
            "username": "missing_user",
            "password": "password123",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Invalid username or password." in response.data

    with client.session_transaction() as session:
        assert "user_id" not in session


def test_login_strips_username_whitespace(
    app,
    client,
):
    insert_user(
        app,
        username="employee1",
        password="password123",
    )

    response = client.post(
        "/login",
        data={
            "username": "  employee1  ",
            "password": "password123",
        },
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"Login successful." in response.data

    with client.session_transaction() as session:
        assert session["username"] == "employee1"


def test_logout_clears_session(
    client,
):
    with client.session_transaction() as session:
        session["user_id"] = 1
        session["username"] = "employee1"
        session["role"] = "cashier"

    response = client.get(
        "/logout",
        follow_redirects=True,
    )

    assert response.status_code == 200
    assert b"You have been logged out." in response.data

    with client.session_transaction() as session:
        assert "user_id" not in session
        assert "username" not in session
        assert "role" not in session


def test_logout_redirects_to_login(
    authenticated_client,
):
    response = authenticated_client.get(
        "/logout",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


@pytest.mark.parametrize(
    "path",
    [
        "/dashboard",
        "/products",
        "/products/new",
        "/discounts",
        "/orders",
        "/orders/history",
    ],
)
def test_protected_pages_redirect_to_login(
    client,
    path,
):
    response = client.get(
        path,
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


@pytest.mark.parametrize(
    ("path", "data"),
    [
        (
            "/products/new",
            {
                "name": "Unauthorized Product",
                "description": "Should not be created",
                "image_path": "",
                "price": "1.00",
                "stock_quantity": "1",
            },
        ),
        (
            "/orders/1/execute",
            {},
        ),
    ],
)
def test_protected_post_routes_redirect_to_login(
    client,
    path,
    data,
):
    response = client.post(
        path,
        data=data,
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_authenticated_user_can_access_products(
    authenticated_client,
):
    response = authenticated_client.get("/products")

    assert response.status_code == 200
    assert b"Product" in response.data


def test_authenticated_user_is_redirected_from_login(
    authenticated_client,
):
    response = authenticated_client.get(
        "/login",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/dashboard" in response.headers["Location"]


def test_root_redirects_unauthenticated_user_to_login(
    client,
):
    response = client.get(
        "/",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_root_redirects_authenticated_user_to_dashboard(
    authenticated_client,
):
    response = authenticated_client.get(
        "/",
        follow_redirects=False,
    )

    assert response.status_code == 302
    assert "/dashboard" in response.headers["Location"]
