CONTRIBUTING.rst
==============

Contributing to robotframework-pywinauto
========================================

Thank you for your interest in contributing to robotframework-pywinauto! This guide explains how you can contribute to the project.

Types of Contributions
=====================

We welcome various types of contributions:

1. **Code Contributions**
   - Bug fixes
   - New features
   - Performance improvements
   - Refactoring

2. **Documentation**
   - Improving existing documentation
   - Adding new documentation
   - Translations

3. **Tests**
   - Writing new test cases
   - Improving existing tests
   - Testing on different platforms

4. **Issue Reporting**
   - Reporting bugs
   - Suggesting new features
   - Providing feedback

5. **Community Support**
   - Answering questions
   - Helping other users
   - Promoting the library

Contribution Process
====================

1. **Find or Create an Issue**
   - Before starting work, check if there's already an issue for what you want to work on
   - If not, create a new issue describing your proposed change
   - Discuss your approach with the maintainers

2. **Fork the Repository**
   - Fork the repository on GitHub
   - Clone your fork locally

3. **Set Up Development Environment**
   - Install dependencies: `pip install -e .[dev]`
   - Run tests to ensure everything works: `pytest`

4. **Create a Branch**
   - Create a new branch for your changes
   - Use a descriptive branch name (e.g., `fix-issue-123` or `add-new-feature`)

5. **Make Changes**
   - Follow the code style guidelines
   - Write tests for your changes
   - Update documentation if necessary

6. **Run Tests**
   - Run all tests to ensure your changes don't break anything
   - Run linting: `flake8`
   - Run type checking: `mypy`

7. **Commit Changes**
   - Use a clear and descriptive commit message
   - Follow the commit message guidelines

8. **Push Changes**
   - Push your changes to your fork

9. **Create a Pull Request**
   - Create a pull request from your branch to the main repository
   - Reference the issue number in the pull request description
   - Describe your changes in detail

10. **Review Process**
    - Maintainers will review your pull request
    - Address any feedback
    - Make additional changes if requested

11. **Merge**
    - Once approved, your changes will be merged

Development Environment Setup
============================

### Prerequisites

- Python 3.8 or later
- Git

### Installation Steps

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
   pytest
   ```

Code Style Guidelines
====================

### Python Style

- Follow PEP 8 guidelines
- Use 4 spaces for indentation (not tabs)
- Limit lines to 100 characters
- Use descriptive variable and function names
- Add docstrings for all functions and classes
- Use type hints for function parameters and return values

### Robot Framework Style

- Follow Robot Framework's style guide
- Use consistent keyword names
- Add proper documentation for keywords
- Use meaningful test case names

### Git Commit Messages

- Start with a short summary (50 characters or less)
- Use the imperative mood ("Fix bug" not "Fixed bug" or "Fixes bug")
- Add a more detailed description if needed (separated by a blank line)
- Reference issues with `#issue-number`

Example:

```
Fix element not found error in Wait Until Element Contains Text

- Fixed incorrect locator handling in the waiting keyword
- Added proper error messages
- Updated tests

Fixes #123
```

Testing
=======

### Running Tests

#### Unit Tests

```bash
pytest
```

#### Acceptance Tests

```bash
robot atest/
```

### Test Coverage

- Aim for high test coverage
- Write tests for all new functionality
- Ensure existing tests pass

Documentation
=============

- Update documentation when adding new features
- Keep documentation clear and concise
- Use examples to illustrate usage
- Follow the existing documentation style

Code of Conduct
===============

We expect all contributors to adhere to our Code of Conduct:

- Be respectful and inclusive
- Listen to others
- Accept constructive criticism
- Focus on the project's best interests
- Avoid personal attacks
- Be professional

Review Process
==============

- All pull requests are reviewed by at least one maintainer
- Reviews focus on code quality, functionality, and adherence to guidelines
- Reviews may include requests for changes
- Once approved, pull requests are merged by a maintainer

Release Process
==============

1. Update version number in `src/pywinautoLibrary/__init__.py`
2. Update `CHANGES.rst` with release notes
3. Create a release on GitHub
4. Publish to PyPI

Getting Help
============

- If you need help, feel free to ask in the issue tracker
- Join the Robot Framework Slack channel for discussion

Thank you for contributing to robotframework-pywinauto!
