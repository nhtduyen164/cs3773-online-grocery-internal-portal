from functools import wraps

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from grocery_portal.db import get_db

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

    query = """
        SELECT id,
               name,
               description,
               image_path,
               price,
               stock_quantity,
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

    query += " ORDER BY name"

    products = db.execute(query, parameters).fetchall()

    total_skus = len(products)

    low_stock_count = sum(
        1 for product in products
        if 0 < product["stock_quantity"] <= 50
    )

    return render_template(
        "products.html",
        products=products,
        total_skus=total_skus,
        low_stock_count=low_stock_count,
        search=search,
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
        price = request.form.get("price", "").strip()
        stock_quantity = request.form.get("stock_quantity", "").strip()

        if not name:
            flash("Product name is required.", "danger")
            return render_template("product_form.html", product=None, form_type="Create")

        try:
            price = float(price)
            if price < 0:
                raise ValueError
        except ValueError:
            flash("Price must be a valid non-negative number.", "danger")
            return render_template("product_form.html", product=None, form_type="Create")

        try:
            stock_quantity = int(stock_quantity)
            if stock_quantity < 0:
                raise ValueError
        except ValueError:
            flash("Quantity must be a valid whole number.", "danger")
            return render_template("product_form.html", product=None, form_type="Create")

        db.execute(
            """
            INSERT INTO products (name, description, image_path, price, stock_quantity)
            VALUES (?, ?, ?, ?, ?)
            """,
            (name, description, image_path, price, stock_quantity),
        )
        db.commit()

        flash("Product created successfully.", "success")
        return redirect(url_for("main.products"))

    return render_template("product_form.html", product=None, form_type="Create")


@main_bp.route("/products/<int:product_id>/edit", methods=["GET", "POST"])
@login_required
def edit_product(product_id):
    db = get_db()

    product = db.execute(
        "SELECT * FROM products WHERE id = ?",
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
        price = request.form.get("price", "").strip()
        stock_quantity = request.form.get("stock_quantity", "").strip()

        if not name:
            flash("Product name is required.", "danger")
            return render_template("product_form.html", product=product, form_type="Edit")

        try:
            price = float(price)
            if price < 0:
                raise ValueError
        except ValueError:
            flash("Price must be a valid non-negative number.", "danger")
            return render_template("product_form.html", product=product, form_type="Edit")

        try:
            stock_quantity = int(stock_quantity)
            if stock_quantity < 0:
                raise ValueError
        except ValueError:
            flash("Quantity must be a valid whole number.", "danger")
            return render_template("product_form.html", product=product, form_type="Edit")

        db.execute(
            """
            UPDATE products
            SET name = ?, description = ?, image_path = ?, price = ?, stock_quantity = ?
            WHERE id = ?
            """,
            (name, description, image_path, price, stock_quantity, product_id),
        )
        db.commit()

        flash("Product updated successfully.", "success")
        return redirect(url_for("main.products"))

    return render_template("product_form.html", product=product, form_type="Edit")
