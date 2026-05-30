# Unit Tests

This folder contains simple unit tests and the helper module for learning and demonstration purposes.

Structure

- `mymodule.py` — example module with small functions to test (`sqaure`, `double`).
- `test_mymodule.py` — unittest-based test file for `mymodule.py`.

Prerequisites

- Python 3.7+

Running the tests

- Run a single test file:

```powershell
python -u "unittests\test_mymodule.py"
```

- Or use unittest discovery to run all tests in the `unittests` folder:

```powershell
python -m unittest discover -s unittests -v
```

Notes

- Do not name test files the same as standard library modules (for example, avoid `unittest.py`) — this will shadow the standard library and cause import errors.
- To add tests, create new files named `test_*.py` and put `unittest.TestCase` classes inside.

Contact

- If you need help extending the tests, open an issue or ask for assistance.
