# Copyright 2023-     Robot Framework Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Optional, List

from pywinautoLibrary.base import LibraryComponent
from pywinautoLibrary.errors import WindowNotFound


class WindowManagementKeywords(LibraryComponent):
    """Keywords for managing application windows.

    This class contains keywords for switching, closing, and manipulating application windows.
    """

    def switch_window(self, locator: str) -> None:
        """Switch to a window matching the given locator.

        :param locator: Locator of the window to switch to.
        :type locator: str
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found.
        """
        self.info(f"Switching to window: {locator}")
        try:
            window = self.find_element(locator)
            window.set_focus()
        except Exception:
            raise WindowNotFound(f"Window with locator '{locator}' not found.")

    def close_window(self, locator: Optional[str] = None) -> None:
        """Close a window matching the given locator.

        If no locator is provided, close the current window.

        :param locator: Locator of the window to close.
        :type locator: str
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found.
        """
        self.info(f"Closing window: {locator or 'current'}")
        try:
            if locator:
                window = self.find_element(locator)
            else:
                window = self.ctx.app.top_window()
            window.close()
        except Exception:
            raise WindowNotFound(f"Window with locator '{locator}' not found.")

    def minimize_window(self, locator: Optional[str] = None) -> None:
        """Minimize a window matching the given locator.

        If no locator is provided, minimize the current window.

        :param locator: Locator of the window to minimize.
        :type locator: str
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found.
        """
        self.info(f"Minimizing window: {locator or 'current'}")
        try:
            if locator:
                window = self.find_element(locator)
            else:
                window = self.ctx.app.top_window()
            window.minimize()
        except Exception:
            raise WindowNotFound(f"Window with locator '{locator}' not found.")

    def maximize_window(self, locator: Optional[str] = None) -> None:
        """Maximize a window matching the given locator.

        If no locator is provided, maximize the current window.

        :param locator: Locator of the window to maximize.
        :type locator: str
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found.
        """
        self.info(f"Maximizing window: {locator or 'current'}")
        try:
            if locator:
                window = self.find_element(locator)
            else:
                window = self.ctx.app.top_window()
            window.maximize()
        except Exception:
            raise WindowNotFound(f"Window with locator '{locator}' not found.")

    def restore_window(self, locator: Optional[str] = None) -> None:
        """Restore a window matching the given locator from minimized or maximized state.

        If no locator is provided, restore the current window.

        :param locator: Locator of the window to restore.
        :type locator: str
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found.
        """
        self.info(f"Restoring window: {locator or 'current'}")
        try:
            if locator:
                window = self.find_element(locator)
            else:
                window = self.ctx.app.top_window()
            window.restore()
        except Exception:
            raise WindowNotFound(f"Window with locator '{locator}' not found.")

    def get_window_title(self, locator: Optional[str] = None) -> str:
        """Get the title of a window matching the given locator.

        If no locator is provided, get the title of the current window.

        :param locator: Locator of the window to get the title from.
        :type locator: str
        :return: Title of the window.
        :rtype: str
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found.
        """
        self.info(f"Getting window title: {locator or 'current'}")
        try:
            if locator:
                window = self.find_element(locator)
            else:
                window = self.ctx.app.top_window()
            return window.window_text()
        except Exception:
            raise WindowNotFound(f"Window with locator '{locator}' not found.")

    def wait_for_window(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait for a window matching the given locator to appear.

        :param locator: Locator of the window to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the window. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found within the timeout.
        """
        self.info(f"Waiting for window: {locator}")
        self.find_element(locator, timeout=timeout)

    def get_window_count(self) -> int:
        """Get the number of open windows in the current application.

        :return: Number of open windows.
        :rtype: int
        """
        windows = self.ctx.app.windows()
        count = len(windows)
        self.info(f"Found {count} windows")
        return count

    def is_window_open(self, locator: str) -> bool:
        """Check if a window matching the given locator is open.

        :param locator: Locator of the window to check.
        :type locator: str
        :return: True if the window is open, False otherwise.
        :rtype: bool
        """
        self.info(f"Checking if window is open: {locator}")
        try:
            self.find_element(locator, required=False)
            return True
        except Exception:
            return False

    def activate_window(self, locator: str) -> None:
        """Activate a window matching the given locator (bring it to the foreground).

        :param locator: Locator of the window to activate.
        :type locator: str
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found.
        """
        self.switch_window(locator)
