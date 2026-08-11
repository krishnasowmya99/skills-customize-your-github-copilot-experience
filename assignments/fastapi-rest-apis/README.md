# 📘 Assignment: FastAPI REST APIs

## 🎯 Objective

Build REST API endpoints using the FastAPI framework and Python typing. Learn how to define routes, request models, and responses while handling common HTTP operations.

## 📝 Tasks

### 🛠️ Create API endpoints

#### Description

Build the core FastAPI application with routes for listing, creating, and retrieving items using path and query parameters.

#### Requirements
Completed program should:

- Define a FastAPI app instance
- Implement `GET /items` to return a list of items
- Implement `GET /items/{item_id}` to return a single item by ID
- Use path parameters and return JSON responses
- Respond with `404 Not Found` when an item ID does not exist

### 🛠️ Add request validation and data models

#### Description

Add Pydantic data models for item creation and update the API to validate incoming request data for new items.

#### Requirements
Completed program should:

- Define a Pydantic model for item data with fields like `name`, `description`, and `price`
- Implement `POST /items` to accept validated item data
- Return the created item with its assigned ID
- Use proper HTTP status codes for success and validation errors
