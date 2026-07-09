from functools import wraps

from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from grocery_portal.db import get_db

main_bp = Blueprint("main", __name__)

# Temporary users for sprint 1 login testing
# Later this can be replaced with users from the database
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

# @main_bp.route("/")
# def index():
#    return render_template("index.html")

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