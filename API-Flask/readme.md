# API-Flask

A small Flask-based API demo built around a static in-memory dataset of people.

## Overview

This project exposes simple REST endpoints for:

- returning a welcome message
- retrieving a list of people
- searching by first/last name
- counting records
- retrieving, creating, and deleting people by UUID
- demonstrating response status handling

## Requirements

- Python 3.10+ (or compatible Python 3.x)
- Flask

## Install

1. Create and activate a virtual environment (recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate
   ```
2. Install Flask:
   ```powershell
   pip install flask
   ```

## Run

From the `API-Flask` folder:

```powershell
python server.py
```

The app starts on `http://127.0.0.1:5000` by default.

## Endpoints

- `GET /`
  - Returns: `Hello, World!`

- `GET /no-content`
  - Returns a JSON message with HTTP status `204 No Content`

- `GET /exp`
  - Returns a JSON response object with HTTP status `200 OK`

- `GET /data`
  - Returns all person records as `{"data": [...]}`
  - If no records exist, returns `404`

- `GET /name-search?name=<term>`
  - Searches `first_name` and `last_name` for a case-insensitive match
  - Returns matching results or `404` when no matches are found

- `GET /count`
  - Returns the total number of records in the dataset

- `GET /person/<uuid:id>`
  - Returns the person with the matching UUID
  - Returns `404` if not found

- `DELETE /person/<uuid:id>`
  - Deletes the matching person and returns a success message
  - Returns `404` if not found

- `POST /person`
  - Adds a new person record from a JSON request body
  - Example JSON payload:
    ```json
    {
      "id": "uuid-string",
      "first_name": "Jane",
      "last_name": "Doe",
      "graduation_year": 2026,
      "address": "123 Main St",
      "city": "City",
      "zip": "00000",
      "country": "Country",
      "avatar": "http://example.com/avatar.png"
    }
    ```
  - Returns `201 Created` on success

## Error Handling

- Missing or invalid request parameters return `400 Bad Request`
- Missing resources return `404 Not Found`
- Internal errors return `500 Internal Server Error`

## Notes

- Data is stored in memory only, so changes are lost when the server restarts.
- The sample dataset is defined directly in `server.py`.
