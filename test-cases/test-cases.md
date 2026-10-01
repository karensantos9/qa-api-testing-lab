# Test Cases

## Users

### TC-USR-001
**Title:** Create user with valid data

**Preconditions:**
- API available
- Valid payload

**Request:**
POST /users

**Expected:**
- HTTP 201
- User is created
- Response contains user ID
- Response contains name
- Response contains email

---

### TC-USR-002
**Title:** Create user without email

**Request:**
POST /users

**Expected:**
- HTTP 400 or 422
- Validation error returned
- User is not created