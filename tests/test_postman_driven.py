# ============================================================
# tests/test_postman_driven.py
#
# PURPOSE: This test shows how to reuse data from your 
#          Postman collection JSON file.
#
# Beginners often ask: "Do I have to copy-paste URLs from Postman?"
# The answer is NO! This test reads them automatically.
# ============================================================

import os
import pytest
from utils.postman_loader import (
    load_postman_collection, 
    get_request_by_name, 
    get_endpoint, 
    get_request_body
)

# 1. Load the Postman collection file once for all tests in this file
COLLECTION_PATH = os.path.join(os.path.dirname(__file__), "..", "postman_crud_collection.json")
collection_data = load_postman_collection(COLLECTION_PATH)


def test_create_user_from_postman(api):
    """
    This test gets the 'Create User' request details from Postman
    and sends the exact same request using our automation framework.
    """
    # 2. Get the specific request named "Create User" from the collection
    postman_request = get_request_by_name(collection_data, "Create User")
    
    # 3. Extract the endpoint and body automatically
    endpoint = get_endpoint(postman_request)
    body = get_request_body(postman_request)
    
    print(f"\n📋 Reusing request from Postman: 'Create User'")
    
    # 4. Send the request using our helper
    response = api.post(endpoint, body)
    
    # 5. Verify the result
    assert response.status == 201
    assert response.json()["name"] == body["name"]
    print("✅ Successfully reused Postman data for the test!")


def test_get_users_from_postman(api):
    """
    Example of reusing the GET request endpoint from Postman.
    """
    postman_request = get_request_by_name(collection_data, "Get All Users")
    endpoint = get_endpoint(postman_request)
    
    print(f"\n📋 Reusing request from Postman: 'Get All Users'")
    
    response = api.get(endpoint)
    
    assert response.status == 200
    assert len(response.json()) > 0
    print(f"✅ Successfully fetched {len(response.json())} users using Postman endpoint!")
