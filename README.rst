robotframework-pywinauto
========================

Robot Framework library for Windows desktop application automation using pywinauto.

Introduction
------------

robotframework-pywinauto is a Robot Framework library that provides keywords for
automating Windows desktop applications using the pywinauto library. It follows
the same architectural patterns as SeleniumLibrary, making it easy to use for
users familiar with Robot Framework and SeleniumLibrary.

Key Features
------------

robotframework-pywinauto provides a comprehensive set of keywords for automating Windows desktop applications:

- **Application Management**: Open, close, connect to, and switch between applications
- **Window Management**: Switch, minimize, maximize, and close windows
- **Control Operations**: Find, click, right-click, double-click, and interact with UI controls
- **Text Operations**: Type text, get text, and verify text content
- **Keyboard Operations**: Press keys, combinations, and hotkeys
- **Mouse Operations**: Move, click, drag, and scroll
- **Waiting Mechanisms**: Wait for windows, elements, and text changes
- **Screenshot Capture**: Capture entire screen or specific elements

Architecture
------------

robotframework-pywinauto is built with a modular architecture:

- **Base**: Core functionality and context management
- **Keywords**: Keyword implementations organized by functionality
- **Locators**: Element finding and location strategies
- **Utils**: Utility functions and helper classes
- **Entry**: Command-line interface

Installation
------------

### Prerequisites

- **Operating System**: Windows 10 or later
- **Python**: 3.8 or later
- **pywinauto**: 0.6.8 or later
- **Robot Framework**: 5.0 or later

### Installation Methods

#### Using pip (Recommended)

The recommended installation method is using pip:

.. code:: bash

    pip install robotframework-pywinauto

#### For Development

For development installations, clone the repository and install it in editable mode:

.. code:: bash

    git clone https://github.com/robotframework/robotframework-pywinauto.git
    cd robotframework-pywinauto
    pip install -e .[dev]

#### Manual Installation

1. Download the latest release from GitHub
2. Extract the archive
3. Navigate to the extracted directory
4. Run:

.. code:: bash

    pip install .

Usage
-----

Here's a simple example of using robotframework-pywinauto to automate a Windows application:

.. code:: robotframework

    *** Settings ***
    Library    pywinautoLibrary    timeout=10

    *** Test Cases ***
    Open Notepad and Write Text
        Open Application    notepad.exe
        Wait For Window    Untitled - Notepad
        Click Element    Edit
        Type Text    Hello, Robot Framework!
        Close Application

### More Usage Examples

#### Calculator Automation

.. code:: robotframework

    *** Settings ***
    Library    pywinautoLibrary    timeout=10

    *** Test Cases ***
    Calculator Addition
        Open Application    calc.exe
        Click Element    Seven
        Click Element    Plus
        Click Element    Three
        Click Element    Equals
        Wait Until Element Contains Text    ResultLabel    10
        Close Application

#### Multiple Application Automation

.. code:: robotframework

    *** Settings ***
    Library    pywinautoLibrary    timeout=10

    *** Test Cases ***
    Open Multiple Applications
        ${alias1}=    Open Application    notepad.exe    alias=notepad1
        ${alias2}=    Open Application    calc.exe    alias=calc
        Switch Application    notepad1
        Type Text    Working in Notepad
        Switch Application    calc
        Click Element    Two
        Close All Applications

#### Keyboard and Mouse Operations

.. code:: robotframework

    *** Settings ***
    Library    pywinautoLibrary    timeout=10

    *** Test Cases ***
    Keyboard Shortcuts
        Open Application    notepad.exe
        Type Text    Hello
        Press Keys    Control    a
        Press Keys    Control    c
        Press Keys    Control    v
        Close Application

Keyword Documentation
-------------------- 

For detailed keyword documentation, please see the `Keyword Documentation`_
page.

.. _Keyword Documentation: https://robotframework-pywinauto.readthedocs.io/en/latest/

Contributing
------------

Contributions are welcome! Please see the `CONTRIBUTING.rst`_ file for more
information.

.. _CONTRIBUTING.rst: CONTRIBUTING.rst

Common Issues and Solutions
--------------------------

### Application Not Opening

**Issue**: The application doesn't open when using `Open Application` keyword.

**Solutions**:
- Verify the application path is correct
- Check if the application requires administrative privileges
- Ensure the application is compatible with your Windows version
- Try adding a delay after opening the application

### Element Not Found

**Issue**: The library can't find the element with the given locator.

**Solutions**:
- Use the correct locator strategy (auto_id, control_id, text, etc.)
- Verify the element exists in the current window
- Check if the window title is correct
- Increase the timeout value
- Use `Wait For Element` keyword before interacting with the element

### Text Not Typing

**Issue**: Text isn't being typed into the input field.

**Solutions**:
- Ensure the element has focus before typing
- Try clicking the element first
- Verify the element is editable
- Use `Press Keys` keyword instead of `Type Text` for some applications

### Application Crashes

**Issue**: The application crashes during automation.

**Solutions**:
- Ensure you're using the correct backend (uia is recommended for modern Windows apps)
- Add appropriate delays between operations
- Avoid rapid consecutive operations
- Check if the application has any known issues with automation

### High CPU Usage

**Issue**: The automation script is using high CPU.

**Solutions**:
- Add appropriate delays between operations
- Avoid using too many `Wait Until` keywords with short timeouts
- Use `Sleep` keyword to give the system time to process operations

License
-------

robotframework-pywinauto is licensed under the Apache License 2.0. See the
`LICENSE.txt`_ file for more information.

.. _LICENSE.txt: LICENSE.txt

Support
-------

If you have any questions or issues, please submit them to the `issue tracker`_.

.. _issue tracker: https://github.com/robotframework/robotframework-pywinauto/issues
