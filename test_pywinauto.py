#!/usr/bin/env python
# Test script to verify pywin32 and pywinauto installation

print("Testing pywin32 and pywinauto installation...")

# Test pywin32
try:
    import win32api
    print("✓ win32api imported successfully")
except Exception as e:
    print(f"✗ Failed to import win32api: {e}")

# Test pywinauto
try:
    from pywinauto.application import Application
    print("✓ pywinauto.application.Application imported successfully")
except Exception as e:
    print(f"✗ Failed to import pywinauto.application.Application: {e}")

print("Test completed.")
