# QA API Testing Lab

A hands-on QA portfolio project focused on REST API testing, functional validation, authentication, business rules, and test documentation.

## Project Overview

The purpose of this project is to develop and demonstrate practical skills in Software Quality Assurance (QA), with a focus on API testing.

The project includes a REST API developed with Python and FastAPI, along with functional test scenarios designed and executed using Postman.

## Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT Authentication
- Postman
- REST API
- HTTP
- JSON
- Git
- GitHub

## API Modules

The API is organized into four main modules:

| Module | Description |
|---|---|
| Users | User registration, consultation, update, and deletion |
| Products | Product management and stock control |
| Auth | User authentication and protected routes |
| Orders | Order creation, consultation, update, deletion, and inventory management |

## Testing Scope

The project covers the following testing activities:

- Functional API testing
- Positive and negative scenarios
- HTTP status code validation
- Request and response body validation
- Required field validation
- Data integrity and business rules
- Authentication and authorization using JWT
- Invalid and missing token scenarios
- User data isolation
- Product stock validation
- Order calculations and inventory updates
- Edge cases and error handling

## Test Execution

Functional test scenarios were executed using Postman, with JavaScript assertions in Post-response scripts.

| Module | Test Scenarios |
|---|---:|
| Users | 18 |
| Products | 17 |
| Auth | 8 |
| Orders | 25 |
| **Total** | **68** |

**Execution status:** 68 documented scenarios executed and approved.

## Project Structure

```text
qa-api-testing-lab/
│
├── api/
│   ├── app/
│   │   ├── routers/
│   │   │   ├── auth.py
│   │   │   ├── users.py
│   │   │   ├── products.py
│   │   │   └── orders.py
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── requirements.txt
│   └── sales_api.db
│
├── postman/
│
├── docs/
│
├── test-cases/
│   ├── test-cases.md
│   ├── users.md
│   ├── products.md
│   ├── auth.md
│   └── orders.md
│
├── README.md
└── .gitignore
```

## Running the API Locally

Clone the repository:

```bash
git clone https://github.com/karensantos9/qa-api-testing-lab.git
```

Navigate to the API directory:

```bash
cd qa-api-testing-lab/api
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set the JWT secret key and start the API:

**Windows PowerShell:**

```powershell
$env:SECRET_KEY = "your-secret-key"
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

## Test Documentation

Detailed test scenarios and execution results are available in the `test-cases/` directory.

## Future Improvements

- Automate API tests using Python and pytest.
- Implement automated test execution.
- Generate test execution reports.
- Integrate automated tests into CI/CD using GitHub Actions.

## Author

QA Analyst focused on Software Quality Assurance, API testing, test automation, and continuous improvement.