#!/usr/bin/env python
# Debug script to check DynamicCore keyword registration

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath('src'))

from pywinautoLibrary import pywinautoLibrary
from pywinautoLibrary.keywords.applicationmanagement import ApplicationManagementKeywords
from pywinautoLibrary.utils.dynamiccore import DynamicCore

print("Debugging DynamicCore keyword registration...")

# Create library instance
lib = pywinautoLibrary(timeout=5)
print("Library instance created")

# Check what keywords are registered
print("\nRegistered keywords:")
for keyword in lib._keywords:
    print(f"  - {keyword}")

# Check if open_application is registered
if 'open_application' in lib._keywords:
    print("\n✓ open_application is registered!")
else:
    print("\n✗ open_application is NOT registered!")

# Debug: Check ApplicationManagementKeywords directly
print("\nDebugging ApplicationManagementKeywords:")
amk = ApplicationManagementKeywords(lib)
print("ApplicationManagementKeywords instance created")

# Check attributes of ApplicationManagementKeywords
print("\nAttributes of ApplicationManagementKeywords:")
for attr_name in dir(amk):
    if not attr_name.startswith('_'):
        attr = getattr(amk, attr_name)
        print(f"  - {attr_name}: type={type(attr).__name__}, callable={callable(attr)}")

# Try to manually register keywords
print("\nManually registering keywords:")
dc = DynamicCore([amk])
print("DynamicCore instance created with only ApplicationManagementKeywords")

print("\nKeywords registered by manual DynamicCore:")
for keyword in dc._keywords:
    print(f"  - {keyword}")
