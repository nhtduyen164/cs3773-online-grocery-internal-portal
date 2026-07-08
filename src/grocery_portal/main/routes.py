from flask import Blueprint, render_template
from grocery_portal.db import get_db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def index():
    return render_template("index.html")
