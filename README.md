# Indian Banks GraphQL API

A GraphQL API built using Flask, SQLAlchemy, and Graphene for querying bank and branch information in India. This project uses Indian bank data and exposes a /gql endpoint to perform flexible queries.

---

## 📌 Problem Statement

Design a GraphQL API that allows querying bank and branch information using SQL-based filtering (bank, IFSC, city, etc.).

---

## ⚙️ Tech Stack

* Python
* Flask
* Graphene (GraphQL for Python)
* PostgreSQL
* SQLAlchemy
* pytest (for testing)

---

## 📁 Project Structure

```
indian-banks-api/
├── app/
│   ├── __init__.py              # Initializes the Flask app and GraphQL schema
│   ├── extensions.py            # Database and other extensions
│   ├── models.py                # SQLAlchemy models (Bank and Branch)
│   └── schema.py                # GraphQL schema definitions
│
├── indian_banks/
│   ├── bank_branches.csv        # CSV data (optional)
│   ├── indian_banks.sql         # SQL dump for populating the database
│   └── README.md                # Source data readme
│
├── tests/
│   └── test_query.py            # Pytest-based GraphQL query test
│
├── config.py                    # Database config with Heroku compatibility
├── run.py                       # Entry point to run the Flask app
├── requirements.txt             # Project dependencies
├── .gitignore                   # Files to be ignored by Git
├── Procfile                     # Heroku process declaration
├── runtime.txt                  # Python version for Heroku
└── README.md                    # Project overview (this file)

```

---

## 🗄️ Database & Models

Two models:

* **Bank**: `id`, `name`
* **Branch**: `id`, `ifsc`, `branch`, `address`, `bank_id`

They are connected via a `ForeignKey` relationship.

---

## 🧠 Solution Approach

* Used SQLAlchemy ORM to model the data.
* Created GraphQL types with `graphene_sqlalchemy`.
* Defined a GraphQL schema with `Query` class exposing:

  * `allBanks`
  * `allBranches`
* Added filtering capabilities on the branches query using SQLAlchemy.
* Exposed endpoint at `/gql` using `flask_graphql`.

---

## 🚀 Running Locally

### 1. Clone the repo

```bash
git clone https://github.com/avani-srivastavaa/indian-banks-api.git
cd indian-banks-api
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Setup PostgreSQL and import data

Import SQL dump from [indian\_banks repo](https://github.com/Amanskywalker/indian_banks) into a local PostgreSQL database named `indian_banks`.

Update `config.py` if needed.

### 5. Run the server

```bash
python run.py
```

Visit `http://localhost:5000/gql` to access the GraphiQL interface.

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🕓 Time Taken

Approximately **5–6 hours**, including setup, GraphQL schema design, debugging, and testing.

---

## 🌐 Deployment (Optional)

Supports Heroku deployment. Just update `config.py` to use:

```python
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "fallback_local_uri").replace("postgres://", "postgresql://")
```

---

## 👩‍💻 Author

**Avani Srivastava**
[GitHub](https://github.com/avani-srivastavaa)
