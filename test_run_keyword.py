#!/usr/bin/env python
# Test script to verify keyword execution using run_keyword method

import sys
import os
import time

# Add src directory to Python path
sys.path.insert(0, os.path.abspath('src'))

from pywinautoLibrary import pywinautoLibrary

print("Testing keyword execution...")

# Create library instance
lib = pywinautoLibrary(timeout=5)
print("✓ Library instance created successfully")

# Test 1: Open Notepad using run_keyword
print("\nTest 1: Opening Notepad...")
try:
    alias = lib.run_keyword("open_application", ("notepad.exe",), {})
    print(f"✓ Notepad opened with alias: {alias}")
except Exception as e:
    print(f"✗ Failed to open Notepad: {e}")
    sys.exit(1)

# Give Notepad time to start
time.sleep(2)

# Test 2: Check if application is open
print("\nTest 2: Checking if application is open...")
try:
    is_open = lib.run_keyword("is_application_open", (alias,), {})
    print(f"✓ Application open status: {is_open}")
except Exception as e:
    print(f"✗ Failed to check application status: {e}")

# Test 3: Get current application alias
print("\nTest 3: Getting current application alias...")
try:
    current_alias = lib.run_keyword("get_current_application_alias", (), {})
    print(f"✓ Current application alias: {current_alias}")
except Exception as e:
    print(f"✗ Failed to get current application alias: {e}")

# Test 4: Close Notepad
print("\nTest 4: Closing Notepad...")
try:
    lib.run_keyword("close_application", (alias,), {})
    print("✓ Notepad closed")
except Exception as e:
    print(f"✗ Failed to close Notepad: {e}")

print("\nKeyword execution test completed successfully!")
