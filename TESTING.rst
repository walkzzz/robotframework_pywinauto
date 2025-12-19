TESTING.rst
==========

Testing robotframework-pywinauto
================================

This document describes how to run tests for robotframework-pywinauto and how to write new test cases.

Test Types
=========

robotframework-pywinauto includes several types of tests:

1. **Unit Tests**
   - Test individual components and functions
   - Run with pytest
   - Located in the `utest` directory

2. **Acceptance Tests**
   - Test end-to-end functionality
   - Run with Robot Framework
   - Located in the `atest` directory

3. **Integration Tests**
   - Test interactions between components
   - Run with pytest
   - Located in the `utest` directory

4. **Performance Tests**
   - Test the performance of key functionality
   - Run with pytest
   - Located in the `utest/performance` directory

Test Environment Setup
====================

### Prerequisites

- **Operating System**: Windows 10 or later
- **Python**: 3.8 or later
- **Dependencies**: Install with `pip install -e .[dev]`

### Setting Up the Test Environment

1. **Clone the Repository**
   ```bash
   git clone https://github.com/robotframework/robotframework-pywinauto.git
   cd robotframework-pywinauto
   ```

2. **Install Dependencies**
   ```bash
   pip install -e .[dev]
   ```

3. **Verify Installation**
   ```bash
   pytest --version
   robot --version
   ```

Running Tests
============

### Running Unit Tests

Unit tests are located in the `utest` directory and can be run with pytest:

```bash
# Run all unit tests
pytest

# Run specific test file
pytest utest/test_keywords.py

# Run specific test case
pytest utest/test_keywords.py::TestApplicationManagement::test_open_application

# Run tests with verbose output
pytest -v

# Run tests with coverage
pytest --cov=src/pywinautoLibrary

# Run tests with coverage report
pytest --cov=src/pywinautoLibrary --cov-report=html
```

### Running Acceptance Tests

Acceptance tests are located in the `atest` directory and can be run with Robot Framework:

```bash
# Run all acceptance tests
robot atest/

# Run specific test file
robot atest/acceptance/keywords/application.robot

# Run tests with verbose output
robot -v

# Run tests with output directory
robot -d results atest/

# Run tests with specific variable
robot -v TIMEOUT:30 atest/
```

### Running Integration Tests

Integration tests are located in the `utest/integration` directory and can be run with pytest:

```bash
# Run all integration tests
pytest utest/integration/

# Run specific integration test file
pytest utest/integration/test_integration.py
```

### Running Performance Tests

Performance tests are located in the `utest/performance` directory and can be run with pytest:

```bash
# Run all performance tests
pytest utest/performance/

# Run specific performance test file
pytest utest/performance/test_performance.py
```

Test Case Structure
==================

### Unit Test Structure

Unit tests should follow this structure:

```python
import pytest
from pywinautoLibrary.keywords.applicationmanagement import ApplicationManagementKeywords

class TestApplicationManagement:
    """Test Application Management keywords."""

    def setup_method(self):
        """Setup method for each test."""
        # Setup test environment
        pass

    def teardown_method(self):
        """Teardown method for each test."""
        # Cleanup test environment
        pass

    def test_open_application(self):
        """Test opening an application."""
        # Test implementation
        pass
```

### Acceptance Test Structure

Acceptance tests should follow this structure:

```robotframework
*** Settings ***
Library    pywinautoLibrary    timeout=10
Test Teardown    Close All Applications

*** Test Cases ***
Open Notepad and Write Text
    [Documentation]    Test opening Notepad, writing text, and closing it.
    [Tags]    smoke    regression
    Open Application    notepad.exe
    Wait For Window    Untitled - Notepad
    Click Element    Edit
    Type Text    Hello, Robot Framework!
    Close Application
```

Test Writing Guidelines
=====================

### Unit Tests

1. **Test One Thing at a Time**
   - Each test should focus on a single functionality
   - Use descriptive test names

2. **Use Setup and Teardown**
   - Setup: Prepare the test environment
   - Teardown: Clean up after the test

3. **Use Assertions**
   - Use pytest assertions to verify expected behavior
   - Include descriptive assertion messages

4. **Mock External Dependencies**
   - Mock pywinauto calls when testing keyword logic
   - Use pytest-mock for mocking

5. **Test Edge Cases**
   - Test empty inputs
   - Test invalid inputs
   - Test boundary conditions

### Acceptance Tests

1. **Test End-to-End Scenarios**
   - Test complete user workflows
   - Focus on business value

2. **Use Descriptive Test Names**
   - Name tests after the functionality being tested
   - Use clear and concise names

3. **Add Documentation**
   - Add [Documentation] to each test case
   - Explain what the test does and why it's important

4. **Use Tags**
   - Add tags like smoke, regression, or feature-specific tags
   - Use tags to categorize tests

5. **Use Variables**
   - Use variables for test data
   - Externalize test data when appropriate

6. **Handle Timeouts**
   - Add appropriate timeouts for waiting operations
   - Avoid hardcoded delays

Test Best Practices
==================

1. **Run Tests Regularly**
   - Run tests before committing changes
   - Run tests in CI/CD pipeline

2. **Write Tests for New Features**
   - Write tests when adding new functionality
   - Test both positive and negative scenarios

3. **Keep Tests Independent**
   - Tests should not depend on each other
   - Tests should be able to run in any order

4. **Keep Tests Fast**
   - Avoid unnecessary delays
   - Use efficient test data

5. **Maintain Tests**
   - Update tests when functionality changes
   - Remove obsolete tests
   - Refactor tests to improve maintainability

6. **Use Test Coverage**
   - Aim for high test coverage
   - Focus on critical functionality
   - Use coverage reports to identify gaps

7. **Test on Multiple Platforms**
   - Test on different Windows versions
   - Test on different screen resolutions
   - Test with different display settings

Writing New Tests
================

### Adding a New Unit Test

1. **Create a Test File**
   - Create a new test file in the `utest` directory
   - Name the file `test_<module_name>.py`

2. **Write Test Cases**
   - Follow the unit test structure
   - Test the new functionality

3. **Run the Test**
   - Run the new test to ensure it passes
   - Run all tests to ensure no regressions

### Adding a New Acceptance Test

1. **Create a Test File**
   - Create a new test file in the `atest` directory
   - Name the file `<feature_name>.robot`

2. **Write Test Cases**
   - Follow the acceptance test structure
   - Test the end-to-end workflow

3. **Run the Test**
   - Run the new test to ensure it passes
   - Run all acceptance tests to ensure no regressions

Test Debugging
=============

### Debugging Unit Tests

1. **Use pytest's Debug Mode**
   ```bash
   pytest --pdb utest/test_keywords.py
   ```

2. **Add Print Statements**
   - Add print statements to debug test execution
   - Use pytest's `-s` flag to show print output

3. **Use Logging**
   - Add logging to the code being tested
   - Configure logging level for debugging

### Debugging Acceptance Tests

1. **Use Robot Framework's Debug Mode**
   ```bash
   robot --debugfile debug.log atest/acceptance/keywords/application.robot
   ```

2. **Add Logging**
   - Add `Log` or `Log To Console` keywords to debug test execution
   - Use different log levels (TRACE, DEBUG, INFO)

3. **Use Screenshots**
   - Add `Capture Screenshot` keywords to debug failing tests
   - Use the `--screenshot` option to capture screenshots automatically

4. **Use Variables**
   - Use variables to store intermediate values
   - Log variable values during test execution

Test Coverage
============

### Measuring Test Coverage

```bash
# Run tests with coverage
pytest --cov=src/pywinautoLibrary

# Generate HTML coverage report
pytest --cov=src/pywinautoLibrary --cov-report=html

# Generate XML coverage report (for CI/CD)
pytest --cov=src/pywinautoLibrary --cov-report=xml
```

### Coverage Reports

- **HTML Report**: Open `htmlcov/index.html` in a browser
- **XML Report**: Use with CI/CD tools like Jenkins or GitHub Actions
- **Console Report**: View coverage summary in the terminal

### Coverage Goals

- **Unit Tests**: Aim for 90%+ coverage
- **Integration Tests**: Aim for 80%+ coverage
- **Acceptance Tests**: Focus on critical workflows

CI/CD Integration
================

robotframework-pywinauto uses GitHub Actions for CI/CD. The CI pipeline:

1. **Runs on Pull Requests**
   - Runs all tests when a pull request is opened or updated
   - Runs on multiple Python versions
   - Runs on different Windows versions

2. **Runs on Main Branch**
   - Runs all tests when changes are merged to main
   - Generates coverage reports
   - Updates documentation

3. **Runs on Release**
   - Runs final tests before release
   - Builds and publishes the package

Continuous Integration Best Practices
====================================

1. **Run Tests Early and Often**
   - Run tests on every commit
   - Run tests on every pull request

2. **Test on Multiple Platforms**
   - Test on different Windows versions
   - Test on different Python versions

3. **Use Parallel Testing**
   - Run tests in parallel to reduce CI time
   - Use pytest-xdist for parallel testing

4. **Fail Fast**
   - Configure CI to fail on the first test failure
   - Use pytest's `-x` flag

5. **Generate Reports**
   - Generate test reports
   - Generate coverage reports
   - Generate linting reports

6. **Notify Teams**
   - Send notifications for failed builds
   - Use GitHub Actions notifications
   - Integrate with Slack or email

Conclusion
=========

Testing is an essential part of developing robotframework-pywinauto. By following these guidelines, you can write effective tests that ensure the library works correctly and reliably. Remember to run tests regularly, maintain high test coverage, and follow best practices for test writing.

If you have any questions about testing, please contact the maintainers through the GitHub issues or the Robot Framework Slack channel.
