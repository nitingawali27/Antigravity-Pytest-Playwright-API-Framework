# ============================================================
# tests/step_defs/test_crud_steps.py
#
# PURPOSE: Step Definitions — the actual Python code that runs
#          for each step in the .feature file.
#
# HOW IT WORKS:
#   - Each function below is mapped to a line in the .feature file
#   - The @given / @when / @then decorators do the mapping
#   - The text inside the decorator MUST match the feature file line
#
# IMPORTANT: pytest-bdd requires test files to start with "test_"
# ============================================================

import pytest
from pytest_bdd import scenarios, given, when, then, parsers

# Load all scenarios from the feature file.
scenarios("crud_users.feature")


# ============================================================
# SHARED STATE: We use a simple dictionary to store data
# between steps. For example: store the response in @when,
# then check it in @then.
# ============================================================

# Module-level variable to store the API response between steps
response_store = {}


# ============================================================
# ✅ GIVEN STEPS — Setup / Precondition
# These run first and set up what we need before the test action.
# ============================================================

@given(parsers.parse('I have the API base URL "{url}"'))
def set_base_url(url):
    """
    Store the base URL so we know where to send requests.
    """
    print(f"\n[URL] Using base URL: {url}")


# ============================================================
# ✅ WHEN STEPS — Actions (the actual API calls)
# ============================================================

@when(parsers.parse('I send a GET request to "{endpoint}"'))
def send_get_request(api, endpoint):
    """
    Send a GET request and store the response.
    """
    response = api.get(endpoint)
    # Store the response so @then steps can check it
    response_store["response"] = response
    response_store["json"] = api.get_json(response)


@when(parsers.parse('I send a POST request to "{endpoint}" with name "{name}" and email "{email}"'))
def send_post_request(api, endpoint, name, email):
    """
    Send a POST request with basic user data.
    """
    body = {
        "name": name,
        "email": email
    }
    print(f"\n[BODY] Sending POST body: {body}")
    response = api.post(endpoint, body)
    response_store["response"] = response
    response_store["json"] = api.get_json(response)


@when(parsers.parse('I send a PUT request to "{endpoint}" with updated name "{name}"'))
def send_put_request(api, endpoint, name):
    """
    Send a PUT request to update the user name.
    """
    body = {"name": name}
    print(f"\n[BODY] Sending PUT body: {body}")
    response = api.put(endpoint, body)
    response_store["response"] = response
    response_store["json"] = api.get_json(response)


@when(parsers.parse('I send a DELETE request to "{endpoint}"'))
def send_delete_request(api, endpoint):
    """
    Send a DELETE request to remove a resource.
    """
    response = api.delete(endpoint)
    response_store["response"] = response
    try:
        response_store["json"] = api.get_json(response)
    except Exception:
        response_store["json"] = {}  # DELETE often returns an empty body


# ============================================================
# ✅ THEN STEPS — Assertions (checking the results)
# ============================================================

@then(parsers.parse('the response status code should be {status_code:d}'))
def check_status_code(status_code):
    """
    Verify the HTTP status code of the last response.
    """
    actual_status = response_store["response"].status
    print(f"\n[CHECK] Expected status: {status_code}, Actual status: {actual_status}")

    # This is the assertion — if it fails, the test fails
    assert actual_status == status_code, (
        f"FAILED: Expected status {status_code} but got {actual_status}"
    )
    print(f"SUCCESS: Status code {status_code} matched!")


@then("the response should return a list of users")
def check_response_is_list():
    """
    Verify the response body is a list (array of users).
    """
    data = response_store["json"]
    print(f"\n[CHECK] Response is a list: {isinstance(data, list)}")
    print(f"   Total users returned: {len(data)}")

    assert isinstance(data, list), f"FAILED: Expected a list but got {type(data)}"
    assert len(data) > 0, "FAILED: Expected at least one user in the list, but got empty!"
    print(f"SUCCESS: Got {len(data)} users!")


@then(parsers.parse('the response should contain the field "{field}" with value "{value}"'))
def check_response_field(field, value):
    """
    Verify that the response JSON contains a specific field with a specific value.
    """
    data = response_store["json"]
    print(f"\n[CHECK] Checking field '{field}' in response...")
    print(f"   Expected: {value}")
    print(f"   Actual  : {data.get(field)}")

    # Convert both to string for comparison (JSON may return int for "id")
    actual_value = str(data.get(field, ""))
    assert actual_value == value, (
        f"FAILED: Expected '{field}' = '{value}' but got '{actual_value}'"
    )
    print(f"SUCCESS: Field '{field}' matches '{value}'!")
