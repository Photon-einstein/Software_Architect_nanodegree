# Udatracker Starter Code

This directory contains the starter code for the Udatracker project. The initial structure of directories and files is described below.

```
.
├── backend
│   ├── __init__.py
│   ├── app.py
│   ├── in_memory_storage.py
│   ├── order_tracker.py
│   ├── requirements.txt
│   └── tests
│       ├── __init__.py
│       ├── test_api.py
│       └── test_order_tracker.py
├── frontend
│   ├── css
│   │   └── style.css
│   ├── index.html
│   └── js
│       └── script.js
├── pytest.ini
└── README.md
```

Tasks:

1. Install the dependencies (Done)

   ```bash
   pip install -r backend/requirements.txt
   ```

2. Run the app a first time (Done)

   ```bash
   python -m backend.app
   ```

3. Run the unit tests a first time (Done)

   ```bash
   pytest
   ```

4. Run the unit tests only of the Order Tracker (Done)

   ```bash
   pytest backend/tests/test_order_tracker.py
   ```

5. Run only integration tests for the API: (Done)

   ```bash
   pytest backend/tests/test_api.py
   ```

6. Run a single test function by name: (Done)

   ```bash
   pytest -k backend/tests/test_add_order_api_success
   ```

7. Read backend code (Done)
   - app.py (Done)
   - in_memory_storage.py (Done)
   - order_tracker.py (Done)

8. Read backend tests (Done)
   - test_api.py (Done)
   - test_order_tracker.py (Done)

9. Read frontend code (in progress)
   - styles.css (Done)
   - script.js (Done)
   - index.html (Done)
