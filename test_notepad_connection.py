#!/usr/bin/env python
# Test script to verify pywinauto can find Notepad window using different methods

import subprocess
import time
import os

print("Testing Notepad connection methods...")

# Method 1: Use tasklist to check if Notepad is running
print("\nMethod 1: Checking if Notepad is running with tasklist...")
result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq notepad.exe'], capture_output=True, text=True)
print(f"Notepad running: {'notepad.exe' in result.stdout}")

# Method 2: Start Notepad and use os.system
print("\nMethod 2: Starting Notepad with os.system...")
os.system('start notepad.exe')
time.sleep(2)

# Method 3: Check with tasklist again
print("\nMethod 3: Checking if Notepad is running after starting...")
result = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq notepad.exe'], capture_output=True, text=True)
print(f"Notepad running: {'notepad.exe' in result.stdout}")

# Method 4: Try to find window with win32gui
print("\nMethod 4: Trying to find Notepad window with win32gui...")
try:
    import win32gui
    
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                windows.append((hwnd, title))
    
    windows = []
    win32gui.EnumWindows(callback, windows)
    
    print(f"Found {len(windows)} visible windows:")
    notepad_windows = []
    for hwnd, title in windows:
        print(f"  - '{title}'")
        if 'Notepad' in title or 'Untitled' in title:
            notepad_windows.append((hwnd, title))
    
    print(f"\nFound {len(notepad_windows)} Notepad-related windows:")
    for hwnd, title in notepad_windows:
        print(f"  - '{title}' (HWND: {hwnd})")
        
    if notepad_windows:
        print(f"\nNotepad window found successfully!")
except Exception as e:
    print(f"Error finding window with win32gui: {e}")

# Method 5: Try pywinauto with connect
print("\nMethod 5: Trying pywinauto connect...")
try:
    from pywinauto.application import Application
    
    # Try to connect to Notepad
    app = Application(backend='win32').connect(title_re='.*Notepad.*', timeout=5)
    print("Connected to Notepad successfully!")
    
    # Try to find windows
    windows = app.windows()
    print(f"Found {len(windows)} windows with pywinauto:")
    for window in windows:
        title = window.window_text()
        print(f"  - '{title}'")
    
    # Close Notepad
    app.kill()
    print("Closed Notepad successfully!")
except Exception as e:
    print(f"Error with pywinauto connect: {e}")
    
    # Try to kill Notepad anyway
    print("Trying to kill Notepad with taskkill...")
    subprocess.run(['taskkill', '/F', '/IM', 'notepad.exe'], capture_output=True)

print("\nTest completed.")
