# ============================================================
# utils/api_helper.py
#
# PURPOSE: A reusable "helper" to make API requests.
#
# Think of this as a toolbox. Instead of writing the same
# request code again and again in every test, we write it
# ONCE here and just call it wherever we need it.
#
# This uses Playwright's APIRequestContext which works
# purely for HTTP requests — no browser is opened.
# ============================================================

import json  # Used to convert Python dictionaries to JSON strings


class APIHelper:
    """
    A simple helper class for making HTTP API requests.

    Usage:
        helper = APIHelper(playwright, base_url)
        response = helper.get("/users")
    """

    def __init__(self, playwright, base_url: str):
        """
        Set up the API helper.

        :param playwright: The playwright instance (provided by pytest fixture)
        :param base_url:   The base URL of the API (e.g., https://jsonplaceholder.typicode.com)
        """
        # Create a Playwright API request context (like a session for API calls)
        self.request = playwright.request.new_context(base_url=base_url)
        self.logs = []  # To store structured logs for reports

    # ----------------------------------------------------------
    # GET Request — Used to FETCH/READ data
    # Example: GET /users → returns all users
    # ----------------------------------------------------------
    def get(self, endpoint: str):
        """
        Send a GET request to the given endpoint.
        """
        print(f"\n{'='*50}")
        print(f"[GET] {endpoint}")
        print(f"{'='*50}")
        
        response = self.request.get(endpoint)
        resp_json = response.json()
        
        # Save to log for HTML report
        self.logs.append({
            "method": "GET",
            "endpoint": endpoint,
            "status": response.status,
            "response": resp_json
        })
        
        print(f"[STATUS] {response.status}")
        print(f"[RESPONSE BODY]\n{json.dumps(resp_json, indent=2)}")
        print(f"{'='*50}\n")
        return response

    # ----------------------------------------------------------
    # POST Request — Used to CREATE new data
    # Example: POST /users with body → creates a user
    # ----------------------------------------------------------
    def post(self, endpoint: str, body: dict):
        """
        Send a POST request with a JSON body.
        """
        print(f"\n{'='*50}")
        print(f"[POST] {endpoint}")
        print(f"[REQUEST BODY]\n{json.dumps(body, indent=2)}")
        print(f"{'='*50}")

        response = self.request.post(endpoint, data=json.dumps(body),
                                     headers={"Content-Type": "application/json"})
        resp_json = response.json()

        # Save to log for HTML report
        self.logs.append({
            "method": "POST",
            "endpoint": endpoint,
            "request_body": body,
            "status": response.status,
            "response": resp_json
        })
        
        print(f"[STATUS] {response.status}")
        print(f"[RESPONSE BODY]\n{json.dumps(resp_json, indent=2)}")
        print(f"{'='*50}\n")
        return response

    # ----------------------------------------------------------
    # PUT Request — Used to UPDATE existing data
    # Example: PUT /users/1 with new data → updates user 1
    # ----------------------------------------------------------
    def put(self, endpoint: str, body: dict):
        """
        Send a PUT request with a JSON body.
        """
        print(f"\n{'='*50}")
        print(f"[PUT] {endpoint}")
        print(f"[REQUEST BODY]\n{json.dumps(body, indent=2)}")
        print(f"{'='*50}")

        response = self.request.put(endpoint, data=json.dumps(body),
                                    headers={"Content-Type": "application/json"})
        resp_json = response.json()

        # Save to log for HTML report
        self.logs.append({
            "method": "PUT",
            "endpoint": endpoint,
            "request_body": body,
            "status": response.status,
            "response": resp_json
        })
        
        print(f"[STATUS] {response.status}")
        print(f"[RESPONSE BODY]\n{json.dumps(resp_json, indent=2)}")
        print(f"{'='*50}\n")
        return response

    # ----------------------------------------------------------
    # DELETE Request — Used to REMOVE data
    # Example: DELETE /users/1 → deletes user with ID 1
    # ----------------------------------------------------------
    def delete(self, endpoint: str):
        """
        Send a DELETE request to the given endpoint.
        """
        print(f"\n{'='*50}")
        print(f"[DELETE] {endpoint}")
        print(f"{'='*50}")
        
        response = self.request.delete(endpoint)
        
        # Save to log for HTML report
        self.logs.append({
            "method": "DELETE",
            "endpoint": endpoint,
            "status": response.status
        })
        
        print(f"[STATUS] {response.status}")
        print(f"{'='*50}\n")
        return response

    # ----------------------------------------------------------
    # Helper: Parse response body as a Python dictionary
    # ----------------------------------------------------------
    def get_json(self, response) -> dict:
        """
        Extract the JSON body from a response as a Python dictionary.

        :param response: The response object returned from get/post/put/delete
        :return: A Python dictionary of the response body
        """
        return response.json()

    # ----------------------------------------------------------
    # Helper: Get the HTTP status code from a response
    # ----------------------------------------------------------
    def get_status(self, response) -> int:
        """
        Get the HTTP status code from a response.

        :param response: The response object
        :return: Integer status code (e.g., 200, 201, 404)
        """
        return response.status

    # ----------------------------------------------------------
    # Cleanup: Close the API session when tests are done
    # ----------------------------------------------------------
    def dispose(self):
        """
        Close the Playwright API session.
        Always call this after your tests are done.
        """
        self.request.dispose()
