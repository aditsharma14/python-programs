# CRUD Example Project

A minimal Flask-based CRUD (Create, Read, Update, Delete) example demonstrating basic web forms and list management.

## Overview

This project provides a simple in-memory transactions manager with the following capabilities:

- List transactions (Read)
- Add a transaction (Create)
- Edit a transaction (Update)
- Delete a transaction (Delete)

It's intended as a small learning project to demonstrate routing, templates and form handling with Flask.

## Project structure

- `app.py` — main Flask application with routes for listing, adding, editing and deleting transactions
- `templates/` — HTML templates (`transactions.html`, `edit.html`, `form.html`, `search.html`)

## Requirements

- Python 3.8+ (3.11 or 3.13 recommended)
- Flask

Install dependencies (recommended inside a virtual environment):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install flask
```

## Running the app

From the project folder (`CRUD`):

```powershell
python app.py
```

Open your browser at `http://127.0.0.1:5000/` to view the transactions list.

## Notes and tips

- The app uses an in-memory list for transactions—data will be lost when the server restarts. For persistence, integrate a database (SQLite, PostgreSQL, etc.).
- To use a different root template name, update the `app.py` route that renders the main page.
- If you see `TemplateNotFound` errors, ensure you run the app from the `CRUD` folder so Flask can locate the `templates/` directory.

## Next steps (optional)

- Add validation for form inputs and better error handling.
- Replace the in-memory storage with a small SQLite database using `sqlite3` or `SQLAlchemy`.
- Add tests for route handlers using Flask's test client.

---

If you want, I can also create a `requirements.txt` and add short development instructions (formatting, linting, tests). Which would you prefer next?
