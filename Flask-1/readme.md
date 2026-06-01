# Flask-1

A small Flask application that serves a single route at `/` and returns `Hello, World!`.

## Project structure

- `server.py` - Flask application entry point.

## Requirements

- Python 3.x
- Flask

## Installation

1. Create a virtual environment (recommended):

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. Install Flask:

   ```powershell
   pip install flask
   ```

## Run the app

```powershell
python server.py
```

Then open `http://127.0.0.1:5000/` in your browser.

## Notes

- The app runs in debug mode by default when executed directly.
- Modify `server.py` to add more routes or change the response.
