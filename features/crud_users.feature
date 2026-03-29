# ============================================================
# features/crud_users.feature
#
# This is a FEATURE FILE — it describes what the tests should do
# in plain English. Even a non-technical person can read this!
#
# FORMAT:
#   Feature  → What feature are we testing?
#   Scenario → One specific test case
#   Given    → The starting condition / setup
#   When     → The action we perform (e.g., send API request)
#   Then     → What we expect to happen (the assertion)
# ============================================================

Feature: User CRUD API Operations
  As a tester,
  I want to test the User API,
  So that I can verify Create, Read, Update, and Delete work correctly.


  # ----------------------------------------------------------
  # TEST 1: Create a new user
  # ----------------------------------------------------------
  Scenario: Create a new user successfully
    Given I have the API base URL "https://jsonplaceholder.typicode.com"
    When I send a POST request to "/users" with name "Nitin Gawali" and email "nitin@test.com"
    Then the response status code should be 201
    And the response should contain the field "name" with value "Nitin Gawali"


  # ----------------------------------------------------------
  # TEST 2: Get all users
  # ----------------------------------------------------------
  Scenario: Get all users successfully
    Given I have the API base URL "https://jsonplaceholder.typicode.com"
    When I send a GET request to "/users"
    Then the response status code should be 200
    And the response should return a list of users


  # ----------------------------------------------------------
  # TEST 3: Get a specific user by ID
  # ----------------------------------------------------------
  Scenario: Get a user by ID
    Given I have the API base URL "https://jsonplaceholder.typicode.com"
    When I send a GET request to "/users/1"
    Then the response status code should be 200
    And the response should contain the field "id" with value "1"


  # ----------------------------------------------------------
  # TEST 4: Update an existing user
  # ----------------------------------------------------------
  Scenario: Update a user successfully
    Given I have the API base URL "https://jsonplaceholder.typicode.com"
    When I send a PUT request to "/users/1" with updated name "Updated Name"
    Then the response status code should be 200
    And the response should contain the field "name" with value "Updated Name"


  # ----------------------------------------------------------
  # TEST 5: Delete a user
  # ----------------------------------------------------------
  Scenario: Delete a user successfully
    Given I have the API base URL "https://jsonplaceholder.typicode.com"
    When I send a DELETE request to "/users/1"
    Then the response status code should be 200
