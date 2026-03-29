# 🚀 API Automation Framework

### Beginner-friendly API Testing with Playwright + Pytest + BDD

This framework is built to be modern, easy to understand, and extremely powerful for testing REST APIs. It uses **Playwright** for lightning-fast API requests and **pytest-bdd** for writing tests in plain English.

---

## 📂 Project Structure

```
api_automation/
│
├── features/                        ← Plain English test scenarios (.feature)
│   └── crud_users.feature           ← BDD test cases for CRUD operations
│
├── tests/                           ← Python test code
│   ├── conftest.py                  ← Setup/teardown (fixtures + reporting)
│   ├── step_defs/
│   │   └── test_crud_steps.py       ← Step definitions (connects feature ↔ code)
│   └── test_postman_driven.py       ← Example: Reuse data from Postman JSON
│
├── utils/                           ← Reusable helpers/tools
│   ├── api_helper.py                ← Makes API calls (GET, POST, etc.)
│   └── postman_loader.py            ← Reads URLs/data from Postman collection
│
├── reports/                         ← Auto-generated HTML test reports (timestamped)
│
├── requirements.txt                 ← Python packages to install
├── pytest.ini                       ← Pytest configuration
└── README.md                        ← This file!
```

---

## ✨ Features (Walkthrough)

### 📊 1. Dynamic Timestamped Reporting
Every time you run your tests, a new report is born! No more overwriting old results.
- **Filename**: `reports/report_20260330_000408.html` (Example)
- **Content**: Self-contained HTML with all logs and results embedded.

### 📝 2. Crystal Clear Logging
The framework logs everything so you don't have to guess what happened:
- **[GET/POST/PUT/DELETE]**: Clearly shows which endpoint was hit.
- **[REQUEST BODY]**: Shows exactly what data you sent.
- **[STATUS]**: Displays the HTTP response code.
- **[RESPONSE BODY]**: Prints the full JSON response, beautifully formatted.

### 🔁 3. Postman Collection Reuse
Stop copy-pasting from Postman! Our `postman_loader.py` can read your `.json` collection directly. Check out `tests/test_postman_driven.py` to see how it automatically grabs the URL, method, and body.

---

## ⚙️ Setup (One-time)

1. **Activate your environment**:
   ```bash
   # Windows
   venv\Scripts\activate
   ```
2. **Install requirements**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Install Playwright browsers**:
   ```bash
   playwright install
   ```

---

## ▶️ Running Tests

### ✅ Run ALL tests (Best for generating reports)
```bash
pytest
```

### ✅ Run only BDD tests
```bash
pytest tests/step_defs/test_crud_steps.py
```

### ✅ Run only Postman-driven tests
```bash
pytest tests/test_postman_driven.py
```

### ✅ Run with live console logging
```bash
pytest -s
```

---

## 📖 Adding a New Test

1. **Feature**: Add a scenario to a `.feature` file in `features/`.
2. **Step Def**: Map the steps in `tests/step_defs/`.
3. **Helper**: Use the `api` fixture to send requests.

---

## 🌐 API Used: JSONPlaceholder
This project uses [JSONPlaceholder](https://jsonplaceholder.typicode.com) for simulation. Note that it doesn't actually save changes to its database, which is perfect for continuous testing!
