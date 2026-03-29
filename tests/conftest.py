# ============================================================
# tests/conftest.py
#
# PURPOSE: This is the "setup & teardown" file for Pytest.
#
# "Fixtures" defined here are automatically available in
# ALL test files — no need to import them manually.
#
# Think of fixtures like:
#   - Before hook → opens the browser/API session
#   - After hook  → closes/cleans up the session
# ============================================================

import os
import pytest
from datetime import datetime
from playwright.sync_api import sync_playwright
from utils.api_helper import APIHelper
import json

# The base URL for all our API tests
# This comes from the Postman collection
BASE_URL = "https://jsonplaceholder.typicode.com"


# ============================================================
# 📊 Dynamic Reporting (Timestamped)
# ============================================================
def pytest_configure(config):
    """
    Sets up the HTML report file name with a unique timestamp.
    Example: reports/report_20260329_2340.html
    """
    # Create reports directory if it doesn't exist
    report_dir = os.path.join(os.getcwd(), "reports")
    if not os.path.exists(report_dir):
        os.makedirs(report_dir, exist_ok=True)

    # Dynamic or Fixed Reporting?
    if os.getenv("GITHUB_ACTIONS") == "true":
        # In CI (GitHub Actions), use a FIXED name for the artifact uploader
        report_name = os.path.join(report_dir, "report.html")
    else:
        # Locally, use a UNIQUE timestamp so you have a history of reports
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_name = os.path.join(report_dir, f"report_{timestamp}.html")

    # Apply the report path to pytest-html
    config.option.htmlpath = report_name
    print(f"\n[REPORT] Saved to: {report_name}")


# ============================================================
# 📝 HTML Report Hooks (pytest-html)
# ============================================================
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook catches the test result and adds custom HTML.
    We grab the API logs from the 'api' fixture and put them
    directly into the report!
    """
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extra", [])

    if report.when == "call":
        # Get our APIHelper from the test item (attached in the fixture)
        api_helper = getattr(item, "_api_helper", None)
        
        if api_helper and api_helper.logs:
            # Format the logs as a nice HTML block
            log_entries = []
            for log in api_helper.logs:
                entry = f"<b>{log['method']} {log['endpoint']}</b> (Status: {log['status']})<br/>"
                if "request_body" in log:
                    entry += f"<i>Request Body:</i><pre>{json.dumps(log['request_body'], indent=2)}</pre>"
                if "response" in log:
                    entry += f"<i>Response Body:</i><pre>{json.dumps(log['response'], indent=2)}</pre>"
                log_entries.append(entry)
            
            # Combine all logs into a single HTML extra
            full_log_html = "<div style='background-color: #f8f9fa; padding: 10px; border: 1px solid #ddd;'>"
            full_log_html += "<hr/>".join(log_entries)
            full_log_html += "</div>"
            
            # Add to the report!
            import pytest_html
            extras.append(pytest_html.extras.html(full_log_html))
            report.extra = extras


@pytest.fixture(scope="function")
def api(request):
    """
    This fixture starts Playwright and creates an API session.
    """
    print("\n[START] Starting Playwright API session...")

    # Start Playwright
    with sync_playwright() as playwright:
        # Create our APIHelper with the base URL
        helper = APIHelper(playwright, BASE_URL)
        
        # Attach the helper to the test item for the reporter hook
        request.node._api_helper = helper

        # "yield" gives the helper to the test
        # Everything after yield runs AFTER the test is done (cleanup)
        yield helper

        # Cleanup: close the session
        helper.dispose()
        print("\n🛑 Playwright API session closed.")


@pytest.fixture
def context_data():
    """
    A simple dictionary to share data BETWEEN steps in a scenario.

    Example: Store the response from step 1, and use it in step 2.

    This is called "scenario context" — it lives only for one test.
    """
    return {}
