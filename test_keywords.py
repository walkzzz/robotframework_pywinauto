#!/usr/bin/env python
# Test script to check what keywords are registered on the library instance

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.abspath('src'))

from pywinautoLibrary import pywinautoLibrary

print("Testing keyword registration...")

# Create library instance
lib = pywinautoLibrary(timeout=5)
print("✓ Library instance created successfully")

# Check what keywords are available
print("\nAvailable keywords:")
try:
    # Get keyword names from the library
    keyword_names = lib.get_keyword_names()
    print(f"Found {len(keyword_names)} keywords:")
    for name in sorted(keyword_names):
        print(f"  - {name}")
except Exception as e:
    print(f"✗ Failed to get keyword names: {e}")

# Check attributes of the library instance
print("\nLibrary instance attributes:")
attributes = [attr for attr in dir(lib) if not attr.startswith('_')]
print(f"Found {len(attributes)} public attributes:")
for attr in sorted(attributes):
    print(f"  - {attr}")

# Check what's in _keywords dictionary
print("\nKeywords in _keywords dictionary:")
if hasattr(lib, '_keywords'):
    keywords = lib._keywords
    print(f"Found {len(keywords)} keywords in _keywords:")
    for name in sorted(keywords.keys()):
        print(f"  - {name}")
else:
    print("✗ No _keywords attribute found")

print("\nKeyword registration test completed!")
