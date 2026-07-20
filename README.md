# Course: CS 3773 - Software Engineering
## Project Option 2: Online Grocery Internal Portal
### Project Overview

This project is creating a backend system design for an internal staff portal of an online grocery store. The system allows internal staff to authenticate and manage products, inventory levels, pricing, discounts, sale items, and customer orders.

The portal is intended for internal users, not customers. Staff members will be able to log in, manage product infomation, track inventory, search and sort products, browse and execute orders.

### Proposed Tech Stack:
  - Python
  - Flask
  - SQLite
  - HTML/CSS
  - Bootstrap
  - Github (for version control)

### Main Features
- Database-backed staff authentication
- Product catalog management
- Inventory tracking
- Product search and sorting
- Discount management
- Sale item management
- Customer order management

### Milestone 1 Deliverables: Testable User Stories **(Due June 30)**
  - [x] Testable User Stories
  - [x] Natural language test cases for each user story
  - [x] UML Class Diagram
  - [x] UML State Diagram (for one important class)

### Milestone 2 Deliverables: Implementation and Testing (comming up)

### Structure
  ```
  docs/       Project documentation, user stories, test cases, and UML diagrams 
  src/        Application source code 
  database/   Database schema and seed data 
  tests/      Unit tests
  ```

### Team Members:
  - Cameron Ortiz
  - Chapell Carr
  - Esteban Fuentes
  - Myar Nguyen

### How to Run

#### 1. Clone the repository and enter the project folder

```bash
git clone <repository-url>
cd cs3773-online-grocery-internal-portal
```

#### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

#### 3. Activate the virtual environment

Linux or WSL:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

#### 4. Install the required packages

```bash
python -m pip install -r requirements.txt
```

#### 5. Initialize the SQLite database

```bash
flask --app src/app.py init-db
```

This creates the database tables using `database/schema.sql` and loads the sample data from `database/seed_data.sql`.

> **Note:** Running this command recreates the SQLite database and reloads the sample data, replacing any existing data.

#### 6. Start the application

```bash
flask --app src/app.py run --debug
```

#### 7. Open the application

Open the following address in a browser:

```text
http://127.0.0.1:5000
```

## Demo User Accounts

| Role | Username | Password |
|------|----------|----------|
| Cashier | employee1 | password123 |
| Manager | manager1 | admin123 |
| Admin | alice_johnson | ADMIN123! |
| Manager | bob_martinez | MANAGER123! |
| Cashier | carla_nguyen | CASHIER123! |

These accounts are automatically created when the database is initialized using the sample seed data.
