from functools import wraps

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from grocery_portal.db import get_db

import sqlite3
from datetime import datetime

main_bp = Blueprint("main", __name__)

# Temporary users for sprint 1 login testing
# This can be replaced with users from the database later
USERS = {
    "employee1": "password123",
    "manager1": "admin123"
}


def login_required(route_function):
    @wraps(route_function)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            flash("Please log in to access this page.", "warning")
            return redirect(url_for("main.login"))
        return route_function(*args, **kwargs)

    return wrapper


@main_bp.route("/")
def index():
    if "username" in session:
        return redirect(url_for("main.dashboard"))
    return redirect(url_for("main.login"))


@main_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "").strip()

        if username in USERS and USERS[username] == password:
            session["username"] = username
            flash("Login successful.", "success")
            return redirect(url_for("main.dashboard"))

        flash("Invalid username or password.", "danger")

    return render_template("login.html")


@main_bp.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "info")
    return redirect(url_for("main.login"))


@main_bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", username=session["username"])


@main_bp.route("/products")
@login_required
def products():
    db = get_db()

    search = request.args.get("search", "").strip()
    sort = request.args.get("sort", "name")

    sort_options = {
        "name": "name ASC",
        "price_asc": """
            CASE
                WHEN is_on_sale = 1 THEN sale_price
                ELSE price
            END ASC
        """,
        "price_desc": """
            CASE
                WHEN is_on_sale = 1 THEN sale_price
                ELSE price
            END DESC
        """,
        "availability": "stock_quantity DESC",
    }

    if sort not in sort_options:
        sort = "name"

    query = """
        SELECT id,
               name,
               description,
               image_path,
               price,
               stock_quantity,
               is_on_sale,
               sale_price,
               created_at
        FROM products
    """

    parameters = []

    if search:
        query += """
            WHERE name LIKE ?
               OR description LIKE ?
        """

        search_pattern = f"%{search}%"
        parameters.extend([search_pattern, search_pattern])

    query += f" ORDER BY {sort_options[sort]}"

    products = db.execute(query, parameters).fetchall()

    total_skus = len(products)

    low_stock_count = sum(
        1 for product in products
        if 0 < product["stock_quantity"] <= 50
    )

    sale_item_count = sum(
        1 for product in products
        if product["is_on_sale"]
    )

    return render_template(
        "products.html",
        products=products,
        total_skus=total_skus,
        low_stock_count=low_stock_count,
        sale_item_count=sale_item_count,
        search=search,
        sort=sort,
    )


@main_bp.route("/products/new", methods=["GET", "POST"])
@login_required
def create_product():
    db = get_db()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        image_path = (
            request.form.get("image_path", "").strip()
            or "images/products/placeholder.png"
        )
        price_input = request.form.get("price", "").strip()
        stock_quantity_input = request.form.get(
            "stock_quantity",
            "",
        ).strip()
        is_on_sale = 1 if request.form.get("is_on_sale") else 0
        sale_price_input = request.form.get(
            "sale_price",
            "",
        ).strip()

        if not name:
            flash("Product name is required.", "danger")
            return render_template(
                "product_form.html",
                product=None,
                form_type="Create",
            )

        try:
            price = float(price_input)

            if price < 0:
                raise ValueError
        except ValueError:
            flash(
                "Price must be a valid non-negative number.",
                "danger",
            )
            return render_template(
                "product_form.html",
                product=None,
                form_type="Create",
            )

        try:
            stock_quantity = int(stock_quantity_input)

            if stock_quantity < 0:
                raise ValueError
        except ValueError:
            flash(
                "Quantity must be a valid whole number.",
                "danger",
            )
            return render_template(
                "product_form.html",
                product=None,
                form_type="Create",
            )

        if is_on_sale:
            if not sale_price_input:
                flash(
                    "Sale price is required when a product is on sale.",
                    "danger",
                )
                return render_template(
                    "product_form.html",
                    product=None,
                    form_type="Create",
                )

            try:
                sale_price = float(sale_price_input)

                if sale_price < 0:
                    raise ValueError
            except ValueError:
                flash(
                    "Sale price must be a valid non-negative number.",
                    "danger",
                )
                return render_template(
                    "product_form.html",
                    product=None,
                    form_type="Create",
                )

            if sale_price >= price:
                flash(
                    "Sale price must be less than the regular price.",
                    "danger",
                )
                return render_template(
                    "product_form.html",
                    product=None,
                    form_type="Create",
                )
        else:
            sale_price = None

        db.execute(
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
                description or None,
                image_path,
                price,
                stock_quantity,
                is_on_sale,
                sale_price,
            ),
        )
        db.commit()

        flash("Product created successfully.", "success")
        return redirect(url_for("main.products"))

    return render_template(
        "product_form.html",
        product=None,
        form_type="Create",
    )


@main_bp.route(
    "/products/<int:product_id>/edit",
    methods=["GET", "POST"],
)
@login_required
def edit_product(product_id):
    db = get_db()

    product = db.execute(
        """
        SELECT
            id,
            name,
            description,
            image_path,
            price,
            stock_quantity,
            is_on_sale,
            sale_price,
            created_at
        FROM products
        WHERE id = ?
        """,
        (product_id,),
    ).fetchone()

    if product is None:
        flash("Product not found.", "danger")
        return redirect(url_for("main.products"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        image_path = (
            request.form.get("image_path", "").strip()
            or "images/products/placeholder.png"
        )
        price_input = request.form.get("price", "").strip()
        stock_quantity_input = request.form.get(
            "stock_quantity",
            "",
        ).strip()
        is_on_sale = 1 if request.form.get("is_on_sale") else 0
        sale_price_input = request.form.get(
            "sale_price",
            "",
        ).strip()

        if not name:
            flash("Product name is required.", "danger")
            return render_template(
                "product_form.html",
                product=product,
                form_type="Edit",
            )

        try:
            price = float(price_input)

            if price < 0:
                raise ValueError
        except ValueError:
            flash(
                "Price must be a valid non-negative number.",
                "danger",
            )
            return render_template(
                "product_form.html",
                product=product,
                form_type="Edit",
            )

        try:
            stock_quantity = int(stock_quantity_input)

            if stock_quantity < 0:
                raise ValueError
        except ValueError:
            flash(
                "Quantity must be a valid whole number.",
                "danger",
            )
            return render_template(
                "product_form.html",
                product=product,
                form_type="Edit",
            )

        if is_on_sale:
            if not sale_price_input:
                flash(
                    "Sale price is required when a product is on sale.",
                    "danger",
                )
                return render_template(
                    "product_form.html",
                    product=product,
                    form_type="Edit",
                )

            try:
                sale_price = float(sale_price_input)

                if sale_price < 0:
                    raise ValueError
            except ValueError:
                flash(
                    "Sale price must be a valid non-negative number.",
                    "danger",
                )
                return render_template(
                    "product_form.html",
                    product=product,
                    form_type="Edit",
                )

            if sale_price >= price:
                flash(
                    "Sale price must be less than the regular price.",
                    "danger",
                )
                return render_template(
                    "product_form.html",
                    product=product,
                    form_type="Edit",
                )
        else:
            sale_price = None

        db.execute(
            """
            UPDATE products
            SET name = ?,
                description = ?,
                image_path = ?,
                price = ?,
                stock_quantity = ?,
                is_on_sale = ?,
                sale_price = ?
            WHERE id = ?
            """,
            (
                name,
                description or None,
                image_path,
                price,
                stock_quantity,
                is_on_sale,
                sale_price,
                product_id,
            ),
        )
        db.commit()

        flash("Product updated successfully.", "success")
        return redirect(url_for("main.products"))

    return render_template(
        "product_form.html",
        product=product,
        form_type="Edit",
    )


@main_bp.route("/discounts")
@login_required
def discounts():
    db = get_db()

    discount_rows = db.execute(
        """
        SELECT
            id,
            code,
            description,
            discount_type,
            discount_value,
            starts_at,
            expires_at,
            max_uses,
            times_used,
            is_active,
            created_at
        FROM discounts
        ORDER BY created_at DESC, code ASC
        """
    ).fetchall()

    total_discounts = len(discount_rows)
    active_discounts = sum(
        1 for discount in discount_rows if discount["is_active"]
    )

    return render_template(
        "discounts.html",
        discounts=discount_rows,
        total_discounts=total_discounts,
        active_discounts=active_discounts,
    )


@main_bp.route("/discounts/new", methods=["GET", "POST"])
@login_required
def create_discount():
    if request.method == "POST":
        code = request.form.get("code", "").strip().upper()
        description = request.form.get("description", "").strip()
        discount_type = request.form.get("discount_type", "").strip()
        discount_value_input = request.form.get(
            "discount_value",
            "",
        ).strip()
        starts_at_input = request.form.get("starts_at", "").strip()
        expires_at_input = request.form.get("expires_at", "").strip()
        max_uses_input = request.form.get("max_uses", "").strip()
        is_active = 1 if request.form.get("is_active") else 0

        if not code:
            flash("Discount code is required.", "danger")
            return render_template("discount_form.html")

        if any(character.isspace() for character in code):
            flash(
                "Discount code cannot contain spaces.",
                "danger",
            )
            return render_template("discount_form.html")

        if discount_type not in ("percentage", "fixed"):
            flash(
                "Select a valid discount type.",
                "danger",
            )
            return render_template("discount_form.html")

        try:
            discount_value = float(discount_value_input)

            if discount_value <= 0:
                raise ValueError
        except ValueError:
            flash(
                "Discount value must be a number greater than zero.",
                "danger",
            )
            return render_template("discount_form.html")

        if discount_type == "percentage" and discount_value > 100:
            flash(
                "Percentage discounts cannot exceed 100%.",
                "danger",
            )
            return render_template("discount_form.html")

        try:
            starts_at = (
                datetime.fromisoformat(starts_at_input)
                if starts_at_input
                else None
            )
        except ValueError:
            flash(
                "Start date and time are invalid.",
                "danger",
            )
            return render_template("discount_form.html")

        try:
            expires_at = (
                datetime.fromisoformat(expires_at_input)
                if expires_at_input
                else None
            )
        except ValueError:
            flash(
                "Expiration date and time are invalid.",
                "danger",
            )
            return render_template("discount_form.html")

        if (
            starts_at is not None
            and expires_at is not None
            and expires_at <= starts_at
        ):
            flash(
                "Expiration must be after the start date and time.",
                "danger",
            )
            return render_template("discount_form.html")

        if max_uses_input:
            try:
                max_uses = int(max_uses_input)

                if max_uses <= 0:
                    raise ValueError
            except ValueError:
                flash(
                    "Maximum uses must be a positive whole number.",
                    "danger",
                )
                return render_template("discount_form.html")
        else:
            max_uses = None

        db = get_db()

        try:
            db.execute(
                """
                INSERT INTO discounts (
                    code,
                    description,
                    discount_type,
                    discount_value,
                    starts_at,
                    expires_at,
                    max_uses,
                    is_active
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    code,
                    description or None,
                    discount_type,
                    discount_value,
                    starts_at.isoformat(sep=" ")
                    if starts_at
                    else None,
                    expires_at.isoformat(sep=" ")
                    if expires_at
                    else None,
                    max_uses,
                    is_active,
                ),
            )
            db.commit()
        except sqlite3.IntegrityError:
            flash(
                "A discount with that code already exists.",
                "danger",
            )
            return render_template("discount_form.html")

        flash(
            f"Discount code {code} created successfully.",
            "success",
        )
        return redirect(url_for("main.discounts"))

    return render_template("discount_form.html")
