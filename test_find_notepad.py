#!/usr/bin/env python
# Test script to verify pywinauto can find Notepad window

from pywinauto.application import Application
import time

print("Testing pywinauto window finding...")

# Start Notepad with win32 backend
print("Starting Notepad...")
app = Application(backend='win32').start('notepad.exe')

# Give Notepad time to start
print("Waiting for Notepad to start...")
time.sleep(2)

# Try to find windows
print("Finding windows...")
try:
    windows = app.windows()
    print(f"Found {len(windows)} windows:")
    for window in windows:
        try:
            title = window.window_text()
            print(f"  - '{title}'")
        except Exception as e:
            print(f"  - Error getting title: {e}")
except Exception as e:
    print(f"Error finding windows: {e}")

# Try with title_re
print("\nTrying to find window with title_re='Notepad':")
try:
    notepad_windows = app.windows(title_re='Notepad')
    print(f"Found {len(notepad_windows)} windows with title_re='Notepad':")
    for window in notepad_windows:
        try:
            title = window.window_text()
            print(f"  - '{title}'")
        except Exception as e:
            print(f"  - Error getting title: {e}")
except Exception as e:
    print(f"Error finding window with title_re: {e}")

# Try to get top window
print("\nGetting top window:")
try:
    top_window = app.top_window()
    title = top_window.window_text()
    print(f"Top window title: '{title}'")
except Exception as e:
    print(f"Error getting top window: {e}")

# Try to find by class
print("\nTrying to find window by class 'Notepad':")
try:
    notepad_windows = app.windows(class_name='Notepad')
    print(f"Found {len(notepad_windows)} windows with class 'Notepad':")
    for window in notepad_windows:
        try:
            title = window.window_text()
            print(f"  - '{title}'")
        except Exception as e:
            print(f"  - Error getting title: {e}")
except Exception as e:
    print(f"Error finding window by class: {e}")

# Close Notepad
print("\nClosing Notepad...")
try:
    app.kill()
except Exception as e:
    print(f"Error closing Notepad: {e}")

print("Test completed.")
