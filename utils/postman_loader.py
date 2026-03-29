# ============================================================
# utils/postman_loader.py
#
# PURPOSE: Read data directly from your Postman collection JSON file.
#
# Instead of copy-pasting URLs or request bodies from Postman
# into your test code, this utility reads them automatically
# from the postman_crud_collection.json file.
#
# This means: if you update Postman, the tests pick it up too!
# ============================================================

import json   # To read the JSON file
import os     # To find the file on disk


def load_postman_collection(file_path: str) -> dict:
    """
    Load and return the entire Postman collection as a Python dictionary.

    :param file_path: Full path to the .json Postman collection file
    :return: The collection as a dictionary
    """
    with open(file_path, "r") as f:
        return json.load(f)


def get_request_by_name(collection: dict, request_name: str) -> dict:
    """
    Find a specific request from the Postman collection by its name.

    Example:
        request = get_request_by_name(collection, "Create User")
        # Returns the 'Create User' request details

    :param collection:    The loaded Postman collection dictionary
    :param request_name:  The exact name of the request in Postman (case-sensitive)
    :return: The request dictionary, or None if not found
    """
    for item in collection.get("item", []):
        if item["name"] == request_name:
            return item["request"]
    return None  # Return None if request name is not found


def get_base_url(request: dict) -> str:
    """
    Extract the base URL from a Postman request.

    Example: "https://jsonplaceholder.typicode.com"

    :param request: A Postman request dictionary
    :return: The base URL as a string
    """
    url_info = request.get("url", {})
    protocol = url_info.get("protocol", "https")
    host = ".".join(url_info.get("host", []))  # Join ["jsonplaceholder","typicode","com"]
    return f"{protocol}://{host}"


def get_endpoint(request: dict) -> str:
    """
    Extract just the path (endpoint) from a Postman request.

    Example: "/users/1"

    :param request: A Postman request dictionary
    :return: The endpoint path as a string
    """
    url_info = request.get("url", {})
    path_parts = url_info.get("path", [])
    return "/" + "/".join(path_parts)  # e.g., ["users", "1"] → "/users/1"


def get_request_body(request: dict) -> dict:
    """
    Extract and parse the JSON body from a Postman request.

    :param request: A Postman request dictionary
    :return: The body as a Python dictionary, or empty dict if no body
    """
    body_info = request.get("body", {})
    raw_body = body_info.get("raw", "{}")
    return json.loads(raw_body)  # Convert JSON string to Python dictionary


# ============================================================
# EXAMPLE USAGE (run this file directly to see it work):
# python utils/postman_loader.py
# ============================================================
if __name__ == "__main__":
    # Path to the Postman collection (one folder up from utils/)
    collection_path = os.path.join(
        os.path.dirname(__file__), "..", "postman_crud_collection.json"
    )

    # Load the collection
    collection = load_postman_collection(collection_path)
    print(f"📂 Collection Name: {collection['info']['name']}")
    print(f"📋 Total Requests: {len(collection['item'])}\n")

    # Print details of each request
    for item in collection["item"]:
        req = item["request"]
        print(f"🔹 Name     : {item['name']}")
        print(f"   Method   : {req['method']}")
        print(f"   Base URL : {get_base_url(req)}")
        print(f"   Endpoint : {get_endpoint(req)}")
        print()
