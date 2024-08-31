# Unittests and Integration Tests

## Overview

This project focuses on the creation and implementation of unit tests and integration tests in Python. The purpose of unit testing is to ensure that individual functions within your code return the expected results for various inputs. Integration tests, on the other hand, are used to test code paths end-to-end, ensuring that the different parts of your application interact correctly.

## Project Structure

- **unittest**: A Python testing framework used to create unit tests for individual functions.
- **mock**: A library used for mocking dependencies and external services in unit tests.
- **parameterized**: A library that allows parameterizing tests to run the same test logic with different inputs.

## Learning Objectives

By the end of this project, you should be able to:

- Understand the difference between unit and integration tests.
- Apply common testing patterns such as mocking, parameterization, and fixtures.

## Requirements

- All code will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7.
- All files should end with a new line.
- The first line of all files should be `#!/usr/bin/env python3`.
- Adhere to `pycodestyle` style (version 2.5).
- All files must be executable.
- All modules, classes, and functions should have proper documentation.
- All functions and coroutines must be type-annotated.

## Tasks

### 0. Parameterize a Unit Test

Write unit tests for the `utils.access_nested_map` function. Create the `TestAccessNestedMap` class and use `@parameterized.expand` to test various inputs and their expected outputs.

**File**: `test_utils.py`

### 1. Parameterize a Unit Test for Exceptions

Extend the previous tests to handle exceptions using `assertRaises` with `@parameterized.expand`.

**File**: `test_utils.py`

### 2. Mock HTTP Calls

Test the `utils.get_json` function by mocking HTTP calls with `unittest.mock.patch`. Ensure that the function returns the correct JSON payload for various URLs.

**File**: `test_utils.py`

### 3. Parameterize and Patch

Test the `utils.memoize` decorator by ensuring that a method is only called once, even when accessed multiple times as a property.

**File**: `test_utils.py`

### 4. Parameterize and Patch as Decorators

Unit test the `client.GithubOrgClient.org` method, ensuring that it interacts correctly with the `get_json` method using `@patch` and `@parameterized.expand`.

**File**: `test_client.py`

### 5. Mocking a Property

Test the `_public_repos_url` property of the `GithubOrgClient` class by mocking the `org` property.

**File**: `test_client.py`

### 6. More Patching

Unit test the `public_repos` method of `GithubOrgClient`, ensuring that the correct list of repositories is returned.

**File**: `test_client.py`

### 7. Parameterize

Test the `has_license` method of `GithubOrgClient` using `@parameterized.expand` to check for the presence of specific licenses.

**File**: `test_client.py`

### 8. Integration Test: Fixtures

Implement integration tests for the `GithubOrgClient.public_repos` method using fixtures and parameterized classes.

**File**: `test_client.py`

### 9. Integration Tests

Extend the integration tests to verify that the `public_repos` method correctly handles filtering by license type.

**File**: `test_client.py`

## Execution

To run the tests, use the following command:

```bash
$ python -m unittest path/to/test_file.py



Resources

    unittest — Unit testing framework
    unittest.mock — mock object library
    How to mock a readonly property with mock?
    parameterized
    Memoization

License

This project is © 2024 ALX, All rights reserved.



This README file includes an overview of the project, the learning objectives, task breakdowns, execution instructions, and relevant resources.

