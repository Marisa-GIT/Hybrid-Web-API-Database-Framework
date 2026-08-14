# 🚀 Hybrid Web + API + Database QA Automation Framework

A professional QA automation framework that integrates **Web UI automation, REST API testing, and Database validation** into a single hybrid testing architecture.

This project was developed as part of my QA Automation portfolio to demonstrate how different testing layers can be integrated into reusable, maintainable, and scalable automated workflows.

---

## 🎯 Project Objective

The objective of this project is to build a hybrid QA automation framework capable of validating application workflows across multiple layers:

- Web UI
- REST API
- Database
- End-to-End business workflows

Instead of testing each layer independently, the framework allows UI workflows to be combined with API and database validations through reusable services and validators.

---

## 🏗️ Framework Architecture

```text
                         TESTS
                           │
                           ▼
                  ┌─────────────────┐
                  │  HybridService  │
                  └────────┬────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Web UI Layer      API Layer      Database Layer
       Selenium        Requests           MySQL
          │                │                │
          └────────────────┼────────────────┘
                           │
                           ▼
                  HybridValidator
                           │
                           ▼
                    Test Results

The architecture separates:

- Tests → Define business scenarios.
- HybridService → Orchestrates workflows across different layers.
- Page Objects → Encapsulate UI interactions.
- API clients → Handle REST API communication.
- Repositories → Handle database access.
- HybridValidator → Centralizes validation logic.
- TestDataManager → Provides reusable test data.

```
## 🛠️ Technologies

- Python
- Selenium WebDriver
- Pytest
- Requests
- MySQL
- Page Object Model (POM)
- JSON
- Git & GitHub
- Logging

---

## 📁 Project Structure

```
Hybrid-Web-API-Database-Framework/
|
├───api
│   │   endpoints.py
│   │   response_validator.py
│   │   schemas.py
│   │   __init__.py
│   │
│   ├───clients
│   │       api_client.py
│   │       user_api_client.py
│   └──     __init__.py
│
├───config
│   │   browsers.py
│   │   environment.py
│   │   settings.py
│   └── __init__.py
│
│
├───core
│   │   base_page.py
│   │   driver_factory.py
│   │   logger.py
│   └── __init__.py
│
│
├───data
│       products.json
│       users.json
│
├───database
│   │   base_repository.py
│   │   db_connection.py
│   │   schemas.py
│   │   validators.py
│   │   __init__.py
│   │
│   ├───queries
│   │   └──  user_queries.py
│   │
│   ├───repositories
│   │   │   order_repository.py
│   │   │   product_repository.py
│   │   │   user_repository.py
│   │   └──  __init__.py
│   │
│   │
│   ├───scripts
│   │       001_create_database.sql
│   │       002_create_tables.sql
│   └──     003_seed_data.sql
│
│
├───locators/
│
├───logs/
│
├───pages
│   │   cart_page.py
│   │   checkout_complete_page.py
│   │   checkout_information_page.py
│   │   checkout_overview_page.py
│   │   inventory_page.py
│   └── login_page.py
│
│
├───screenshots/
|
│
├───services
│   │   hybrid_service.py
│   │
│   ├───validators
│       │    hybrid_validator.py
│       └─── __init__.py
│
├───tests
│   ├───api
│   │   │
│   │   └─── test_user_api_client.py
│   │
│   ├───database
│   │   │
│   │   └─── test_user_repository.py
│   │
│   ├───hybrid
│   │   │    test_checkout_flow.py
│   │   │    test_inventory_flow.py
│   │   │    test_user_flow.py
│   │   └─── __init__.py
│   │
│   └───ui/
│
├── utils/
│   └── test_data_manager.py
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

```
## 🧪 Testing Strategy

The framework is divided into four main testing layers.

1. API Testing

Validates REST API functionality including:

- Retrieve all users
- Retrieve user by ID
- User not found scenarios
- HTTP response validation

2. Database Testing

Validates database operations including:

- Retrieve users
- Retrieve user by ID
- User existence
- User not found scenarios

3. UI Testing

Automates the main e-commerce workflows:

- Login
- Inventory
- Shopping cart
- Checkout
- End-to-end purchase

4. Hybrid Testing

Combines multiple layers into a single workflow.

## 🔄 Hybrid User Flow
```
Login
  ↓
Retrieve user from API
  ↓
Retrieve user from Database
  ↓
Validate user identity

The framework verifies that the expected user is correctly retrieved from both API and Database layers.

```
## 🛒 Hybrid Inventory Flow
```
Login
  ↓
Open Inventory
  ↓
Validate product catalog
  ↓
Validate product price
  ↓
Add product to cart
  ↓
Validate cart badge

```

## 🛍️ Hybrid Cart Flow

```
Login
  ↓
Inventory
  ↓
Add product
  ↓
Open Cart
  ↓
Validate product
  ↓
Validate product details

```

## 💳 Hybrid Checkout Flow

```

Login
  ↓
Inventory
  ↓
Add product
  ↓
Cart
  ↓
Checkout
  ↓
Enter customer information
  ↓
Checkout Overview
  ↓
Validate products and totals
  ↓
Complete purchase

```

## 📊 Checkout Validation

The framework validates:

- Product names
- Product prices
- Subtotal
- Tax
- Final total
- Purchase completion message

The subtotal is validated against the sum of the products, while the final total is validated against subtotal + tax.

---

## 📦 Test Data Management

Test data is separated from the test logic using JSON files.

```
Example:

{
    "backpack": {
        "name": "Sauce Labs Backpack",
        "price": 29.99
    }
}

```

Tests retrieve the data through TestDataManager instead of hardcoding credentials and product information directly inside test cases.

This improves:

- Maintainability
- Reusability
- Readability
- Data-driven testing

---

## 🧩 Design Patterns

### Page Object Model

Each application page is represented by a dedicated class.

- LoginPage
- InventoryPage
- CartPage
- CheckoutInformationPage
- CheckoutOverviewPage
- CheckoutCompletePage

This separates UI interactions from test logic.

### Service Layer

HybridService orchestrates complete business workflows.

For example:

purchase_product()

coordinates:

```
Login
→ Inventory
→ Cart
→ Checkout
→ Purchase

```

### Validator Layer

HybridValidator centralizes reusable validation logic instead of duplicating assertions throughout the tests.

---

## 🧪 Test Execution

Run the complete test suite:

pytest -v

Run only hybrid tests:

pytest -v tests/hybrid

Run a specific flow:

pytest -v tests/hybrid/test_inventory_flow.py
✅ Test Results

The complete test suite currently contains:

43 automated tests

43 passed

Coverage includes:

- API tests
- Database tests
- UI tests
- Hybrid workflows
- End-to-end scenarios

---

## 📚 Key Learning Outcomes

Through this project I practiced:

- Designing a multi-layer QA automation framework
- Applying Page Object Model
- Creating reusable service layers
- Separating validation logic from workflow logic
- API automation with Python
- Database validation with MySQL
- UI automation with Selenium
- Data-driven testing with JSON
- Pytest fixtures
- Automated screenshots on test failures
- Logging
- Git workflow and feature branches
- End-to-end business workflow automation

---

## 🚀 Future Improvements

The current version focuses on functionality and framework integration.

Future refactoring and improvements may include:

- Further separation of service responsibilities
- Improved type hints
- Advanced test reporting
- CI/CD with GitHub Actions
- Parallel test execution
- Environment-based configuration
- Improved logging
- Docker integration
- Code quality and static analysis
- Additional API/UI/Database validations

---

## 👩‍💻 Author

Isabel Vides

QA Automation Engineer in Training

This project is part of my QA Automation portfolio and demonstrates my progression from UI automation toward integrated Web + API + Database testing.
