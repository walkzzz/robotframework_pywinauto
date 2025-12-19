#!/usr/bin/env python
# Test basic functionality of the pywinautoLibrary

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath('src'))

from pywinautoLibrary import pywinautoLibrary
import time

print("Testing basic pywinautoLibrary functionality...")

# Create library instance
lib = pywinautoLibrary(timeout=5)
print("✓ Library instance created successfully")

# Start Notepad
print("\nStarting Notepad...")
alias = lib.open_application("notepad.exe")
print(f"✓ Notepad started with alias: {alias}")

# Give Notepad time to start
time.sleep(2)

# Try to get current application
print("\nGetting current application...")
try:
    app = lib.app
    print(f"✓ Current application: {app}")
    print(f"✓ Application process ID: {app.process_id}")
except Exception as e:
    print(f"✗ Failed to get current application: {e}")

# Try to find windows
print("\nFinding application windows...")
try:
    windows = app.windows()
    print(f"✓ Found {len(windows)} windows")
    for window in windows:
        try:
            title = window.window_text()
            print(f"  - '{title}'")
        except Exception as e:
            print(f"  - Error getting title: {e}")
except Exception as e:
    print(f"✗ Failed to find windows: {e}")

# Close Notepad
print("\nClosing Notepad...")
lib.close_application()
print("✓ Notepad closed")

print("\nBasic functionality test completed!")
