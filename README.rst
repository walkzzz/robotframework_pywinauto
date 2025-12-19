robotframework-pywinauto
========================

Robot Framework library for Windows desktop application automation using pywinauto.

Introduction
------------

robotframework-pywinauto is a Robot Framework library that provides keywords for
automating Windows desktop applications using the pywinauto library. It follows
the same architectural patterns as SeleniumLibrary, making it easy to use for
users familiar with Robot Framework and SeleniumLibrary.

Installation
------------

The recommended installation method is using pip:

.. code:: bash

    pip install robotframework-pywinauto

For development installations, clone the repository and install it in editable mode:

.. code:: bash

    git clone https://github.com/robotframework/robotframework-pywinauto.git
    cd robotframework-pywinauto
    pip install -e .[dev]

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

Keyword Documentation
--------------------- 

For detailed keyword documentation, please see the `Keyword Documentation`_
page.

.. _Keyword Documentation: https://robotframework-pywinauto.readthedocs.io/en/latest/

Contributing
------------

Contributions are welcome! Please see the `CONTRIBUTING.rst`_ file for more
information.

.. _CONTRIBUTING.rst: CONTRIBUTING.rst

License
-------

robotframework-pywinauto is licensed under the Apache License 2.0. See the
`LICENSE.txt`_ file for more information.

.. _LICENSE.txt: LICENSE.txt

Support
-------

If you have any questions or issues, please submit them to the `issue tracker`_.

.. _issue tracker: https://github.com/robotframework/robotframework-pywinauto/issues
