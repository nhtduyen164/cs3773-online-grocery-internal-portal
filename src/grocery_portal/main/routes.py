from flask import Blueprint, render_template
from grocery_portal.db import get_db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")

products_bp = Blueprint('products', __name__)

@products_bp.route('/products')
def view_products():
    db = get_db()

    products = db.execute('SELECT name, description, price, stock_quantity FROM products').fetchall()

    return render_template('products.html', products=products)