# Test Strategy

## Scope

The project covers API testing for authentication,
users, products and orders.

## Test Types

### Functional Testing
Validates expected API behavior.

### Negative Testing
Validates invalid inputs and error handling.

### Boundary Testing
Validates values at and around business limits.

### Authentication Testing
Validates authenticated and unauthenticated requests.

### Authorization Testing
Validates access according to user permissions.

### Contract Testing
Validates request and response structure.

## Validation

Each test validates:

- HTTP status code
- Response body
- Response schema
- Business rules
- Error messages when applicable