# Indian Banks GraphQL API

A GraphQL API built with Flask to query Indian bank branches and their related bank data using a PostgreSQL database.

---

## 🔧 Tech Stack

- Python
- Flask
- GraphQL (`flask-graphql`, `graphene`)
- PostgreSQL
- SQLAlchemy
- pytest (for testing)

---

## 🚀 Features

- GraphQL endpoint at `/gql`
- Query bank branches and associated bank details
- Clean and modular Flask app structure
- Sample GraphQL UI via GraphiQL
- Pytest-based test case
- PostgreSQL-backed relational database

---

## 🧪 Sample GraphQL Query

Paste this in the GraphiQL UI at [http://localhost:5000/gql](http://localhost:5000/gql):

```graphql
query {
  allBranches {
    ifsc
    branch
    address
    bank {
      name
    }
  }
}
