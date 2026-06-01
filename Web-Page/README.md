# Maths Project

A simple Flask web application that solves basic math operations: addition, subtraction, and multiplication.

## Project structure

- `server.py` — Flask application routes and request handling
- `maths/mathematics.py` — math helper functions
- `templates/index.html` — web interface for input and results
- `static/` — optional client-side assets

## Features

- `GET /sum?num1=<value>&num2=<value>` — returns the sum of two numbers
- `GET /sub?num1=<value>&num2=<value>` — returns the difference
- `GET /mul?num1=<value>&num2=<value>` — returns the product
- `GET /` — renders the main HTML page

## Setup

1. Create and activate a virtual environment (recommended):
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
2. Install Flask:
   ```powershell
   pip install flask
   ```

## Run the app

From the `Maths-Project` folder:

```powershell
python server.py
```

Then open:

- `http://127.0.0.1:8080/`

## Notes

- Make sure `server.py` is run from the project directory so Flask can find `templates/index.html`.
- The app automatically converts whole-number results to integers for cleaner output.
