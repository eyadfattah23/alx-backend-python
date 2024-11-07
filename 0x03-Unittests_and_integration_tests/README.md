# Unittests and Integration Tests 


## The difference between unit and integration tests.



A **unit test** is a test written by the programmer to verify that a relatively small piece of code is doing what it is intended to do. They are narrow in scope, they should be easy to write and execute, and their effectiveness depends on what the programmer considers to be useful. The tests are intended for the use of the programmer, they are not directly useful to anybody else, though, if they do their job, testers and users downstream should benefit from seeing fewer bugs.

Part of being a unit test is the implication that things outside the code under test are mocked or stubbed out. Unit tests shouldn't have dependencies on outside systems. They test internal consistency as opposed to proving that they play nicely with some outside system.

An integration test is done to demonstrate that different pieces of the system work together. Integration tests can cover whole applications, and they require much more effort to put together. They usually require resources like database instances and hardware to be allocated for them. The integration tests do a more convincing job of demonstrating the system works (especially to non-programmers) than a set of unit tests can, at least to the extent the integration test environment resembles production.

Actually **"integration test"** gets used for a wide variety of things, from full-on system tests against an environment made to resemble production to any test that uses a resource (like a database or queue) that isn't mocked out. At the lower end of the spectrum an integration test could be a junit test where a repository is exercised against an in-memory database, toward the upper end it could be a system test verifying applications can exchange messages.


### ***example: ***

```py3
import requests
import unittest
from unittest.mock import patch, Mock


def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response. json()


class TestUserData(unittest.TestCase):
    @patch('requests.get')
    def test_get_user_data(self, mock_get):
        mock_response = Mock()
        response_dict = {'name': 'John', 'email': 'john@example.com'}
        mock_response.json.return_value = response_dict

        mock_get.return_value = mock_response

        user_data = get_user_data(1)

        mock_get.assert_called_with("https://api.example.com/users/1")

        self.assertEqual(user_data, response_dict)


if __name__ == '__main__':
    unittest.main()
```


#### Explanation:
This code demonstrates a Python function, `get_user_data`, which fetches user data from an API, and a unit test to validate its behavior using the `unittest` library and `unittest.mock` to simulate API responses. Let's go over each part in detail:

### Code Breakdown

#### Imports
```python
import requests
import unittest
from unittest.mock import patch, Mock
```
1. `requests`: This library is used to make HTTP requests.
2. `unittest`: The Python standard library for creating unit tests.
3. `unittest.mock`: Provides utilities for replacing parts of your system under test and verifying interactions. Here, `patch` and `Mock` are used to simulate API responses.

#### `get_user_data` Function
```python
def get_user_data(user_id):
    response = requests.get(f"https://api.example.com/users/{user_id}")
    return response.json()
```
- **Purpose**: This function takes a `user_id` and makes a `GET` request to a fictional API endpoint, `https://api.example.com/users/{user_id}`.
- **Steps**:
  1. It uses `requests.get()` to send a GET request to the API endpoint.
  2. After receiving a response, it calls `.json()` to parse the JSON data from the response and returns it.
- **Example**: If `user_id` is `1`, it would request data from `https://api.example.com/users/1` and return the JSON response.

#### Test Class: `TestUserData`
```python
class TestUserData(unittest.TestCase):
```
This defines a test class inheriting from `unittest.TestCase`, which is necessary to use the `unittest` framework for running tests.

##### `test_get_user_data` Method
```python
@patch('requests.get')
def test_get_user_data(self, mock_get):
```
- **Decorator**: `@patch('requests.get')` temporarily replaces `requests.get` with a mock object, `mock_get`, during the test. This is useful for simulating API calls without actually hitting the API.
- **Parameter**: `mock_get` is passed as an argument to `test_get_user_data`, allowing the test to control and inspect the behavior of `requests.get`.

###### Setting up the Mock Response
```python
mock_response = Mock()
response_dict = {'name': 'John', 'email': 'john@example.com'}
mock_response.json.return_value = response_dict
mock_get.return_value = mock_response
```
1. `mock_response = Mock()`: Creates a `Mock` object to simulate an actual HTTP response.
2. `response_dict`: Defines a dictionary that simulates the expected JSON response.
3. `mock_response.json.return_value = response_dict`: Configures the mock response's `.json()` method to return `response_dict` when called.
4. `mock_get.return_value = mock_response`: Configures `mock_get` to return `mock_response` whenever `requests.get` is called within `get_user_data`.

###### Calling the Function and Asserting Results
```python
user_data = get_user_data(1)
```
- This calls the `get_user_data` function with `user_id = 1`. Because of the `patch`, `requests.get` is replaced by `mock_get`, so it returns `mock_response` instead of making a real API call.

###### Validating the Mock Call and Expected Output
```python
mock_get.assert_called_with("https://api.example.com/users/1")
self.assertEqual(user_data, response_dict)
```
1. `mock_get.assert_called_with(...)`: This assertion verifies that `requests.get` was called with the expected URL.
2. `self.assertEqual(user_data, response_dict)`: Checks if `user_data` (the function’s return value) matches `response_dict`, confirming that `get_user_data` returned the expected data.

#### Running the Tests
```python
if __name__ == '__main__':
    unittest.main()
```
- **Purpose**: This block runs the tests if the script is executed directly. `unittest.main()` automatically discovers and runs all test methods in the script.

### Summary
The `get_user_data` function retrieves user data by making an HTTP request, and `TestUserData` is a unit test for `get_user_data` that:
1. Uses a mock for `requests.get` to simulate the API call.
2. Checks that the function correctly handles and returns JSON data.
3. Validates that the function calls the correct URL with the given user ID.

Let me know if you'd like further clarification on any part of the code!


Using mocks is a powerful technique in testing that allows you to simulate complex dependencies, external services, or system states. By doing so, you can isolate the code under test, ensuring that it behaves as expected without actually triggering those dependencies.

Let's break down the concepts, use cases, and steps for mocking, including how to mock a read-only property.

### What is `Mock` in Python?
`Mock` is part of Python’s `unittest.mock` module, designed to help create simple objects for testing. It allows you to:
- Imitate parts of your code or objects you don’t want to use directly in tests (like database calls, API requests, etc.).
- Set return values for specific method calls.
- Verify how often and with what arguments a method or function is called.

### Why Use Mock?
Mocks are useful in unit testing to:
1. **Isolate tests**: Only test one unit (function, class) without relying on external systems.
2. **Avoid real resource usage**: Prevent unnecessary resource use, like making actual API calls, writing files, or connecting to databases.
3. **Ensure reliability**: Control return values or behaviors, so tests are consistent and not affected by network issues or file I/O.
4. **Test edge cases**: Simulate unusual situations or errors that may be hard to recreate in real life, such as timeouts or network failures.

### How to Use `Mock`
The core usage involves creating a mock object and configuring its behavior or return values as needed.

1. **Creating a Mock Object**:
   ```python
   from unittest.mock import Mock

   my_mock = Mock()
   ```
   This `my_mock` object now acts as a placeholder and can simulate functions, properties, or methods.

2. **Setting Return Values**:
   ```python
   my_mock.some_method.return_value = "Hello, Mock!"
   print(my_mock.some_method())  # Output: "Hello, Mock!"
   ```

3. **Simulating Exceptions**:
   ```python
   my_mock.some_method.side_effect = Exception("An error occurred")
   try:
       my_mock.some_method()
   except Exception as e:
       print(e)  # Output: "An error occurred"
   ```

4. **Verifying Calls**:
   ```python
   my_mock.some_method("test")
   my_mock.some_method.assert_called_with("test")
   ```

### When to Use Mock
Mocks are particularly useful for:
- **API calls**: Prevent hitting external endpoints by simulating API responses.
- **File I/O**: Avoid reading/writing files directly.
- **Database operations**: Don’t modify real data; simulate interactions instead.
- **Time-based operations**: Speed up tests that rely on time (e.g., waiting or delays).
- **Expensive computations**: Replace intensive calculations with simple return values for faster tests.

### Advanced Mocking: Read-Only Properties
Mocking read-only properties (properties without a setter method) can be done by using `PropertyMock` from the `unittest.mock` module. `PropertyMock` allows you to set up a property that behaves like an attribute, returning a fixed value when accessed.

#### Example: Mocking a Read-Only Property
Let’s say we have a class `User` with a read-only property `name`.

```python
from unittest.mock import patch, PropertyMock

class User:
    @property
    def name(self):
        return "Alice"
```

To mock `name` in a test so that it returns a different value, you can do this:

```python
import unittest
from unittest.mock import patch, PropertyMock

class TestUser(unittest.TestCase):
    @patch('__main__.User.name', new_callable=PropertyMock)
    def test_name_property(self, mock_name):
        mock_name.return_value = "Mocked Name"
        user = User()

        self.assertEqual(user.name, "Mocked Name")  # The test will pass, as name is now mocked.
```

#### Explanation:
1. **@patch Decorator**: `@patch('__main__.User.name', new_callable=PropertyMock)` replaces `User.name` with a mock property. The `new_callable=PropertyMock` argument tells `patch` to use `PropertyMock`, which is specialized for mocking properties.
2. **Setting the Return Value**: `mock_name.return_value = "Mocked Name"` sets the return value of the property.
3. **Verification**: The assertion checks that accessing `user.name` returns `"Mocked Name"` instead of `"Alice"`.

### Summary
Mocks are essential tools in testing, allowing for:
- **Controlled and predictable test environments**: By isolating the code from dependencies.
- **Flexible configurations**: Easily set return values or simulate errors.
- **Property mocking**: Mocking even read-only properties with `PropertyMock`.

Would you like to explore more advanced mocking patterns, such as creating side effects or using `patch` in different contexts?
-----


[parameterization](https://medium.com/@samarthgvasist/parameterized-unit-testing-in-python-9be82fa7e17f)

https://pypi.org/project/parameterized/


[task 5 resource](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock):


    Implement the `test_public_repos_url` method to unit-test `GithubOrgClient._public_repos_url`.

    Use patch as a context manager to patch `GithubOrgClient.org` and make it return a known payload.

    Test that the result of `_public_repos_url` is the expected one based on the mocked payload.


----

#### 6. More patching

Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.

Use @patch as a decorator to mock get_json and make it return a payload of your choice.

Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.

Test that the list of repos is what you expect from the chosen payload.

Test that the mocked property and the mocked get_json was called once.
----
