# CS 3773 Software Engineering

## Online Grocery Internal Portal

### Project Overview

The Online Grocery Internal Portal is a Flask-based web application designed for the internal staff of an online grocery store. It allows authorized employees to manage products, inventory, pricing, discounts, sale items, and customer orders.

The application is intended for internal employees rather than customers. Staff members can log in using database-backed accounts, view dashboard information, search and sort products, manage product records, review customer orders, and execute orders while validating available inventory.

## Technology Stack

* Python
* Flask
* SQLite
* HTML and CSS
* Bootstrap
* Pytest
* Git and GitHub

## Main Features

* Database-backed employee authentication
* Login and logout session management
* Role-based access restrictions
* Dashboard with store information and metrics
* Product catalog management
* Product creation and editing
* Inventory and product availability tracking
* Product search by name or description
* Product sorting by price or availability
* Discount code management
* Sale item management
* Customer order listing and order details
* Order sorting by time, customer, or total amount
* Order execution with inventory validation
* Automatic inventory reduction after order execution
* Automatic order status updates
* Unit tests for authentication, products, searching, sorting, and order execution

## Project Structure

```text
database/     Database schema and sample seed data
docs/         User stories with test cases, UML diagrams, backlog, and reports
src/          Flask application source code and templates
tests/        Automated unit tests
requirements.txt
README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/nhtduyen164/cs3773-online-grocery-internal-portal.git
cd cs3773-online-grocery-internal-portal
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

Linux or WSL:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the required packages

```bash
python -m pip install -r requirements.txt
```

### 5. Initialize the SQLite database

```bash
flask --app src/app.py init-db
```

This command creates the database tables using `database/schema.sql` and loads the sample data from `database/seed_data.sql`.

> **Note:** Running this command recreates the SQLite database and reloads the sample data. Any changes stored in the existing database will be replaced.

### 6. Start the application

```bash
flask --app src/app.py run --debug
```

### 7. Open the application

Open the following address in a web browser:

```text
http://127.0.0.1:5000
```

## Demo User Accounts

| Role    | Username        | Password      |
| ------- | --------------- | ------------- |
| Cashier | `employee1`     | `password123` |
| Manager | `manager1`      | `admin123`    |
| Admin   | `alice_johnson` | `ADMIN123!`   |
| Manager | `bob_martinez`  | `MANAGER123!` |
| Cashier | `carla_nguyen`  | `CASHIER123!` |

These demonstration accounts are automatically created when the database is initialized using the sample seed data.

## Running the Tests

With the virtual environment activated, run:

```bash
python -m pytest tests -v
```

The test suite covers product creation and updates, product searching and sorting, authentication, order execution, inventory reduction, and insufficient-inventory validation.

## Project Documentation

Supporting project documentation is located in the `docs` directory and includes:

* Product backlog
* User stories with natural-language test cases
* UML class diagram
* UML state diagram
* Workload distribution report
* LLM usage report

The GitHub repository contains the complete source-code history and team contribution history.

## Team Members

* Cameron Ortiz
* Chapell Carr
* Esteban Fuentes
* Myar Nguyen
