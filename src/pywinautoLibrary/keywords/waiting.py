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

import time
from typing import Optional

from pywinautoLibrary.base import LibraryComponent
from pywinautoLibrary.errors import ElementNotFound


class WaitingKeywords(LibraryComponent):
    """Keywords for waiting operations.

    This class contains keywords for waiting for various conditions in Windows applications,
    such as elements to appear, elements to be enabled, etc.
    """

    def wait_until_element_is_visible(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait until an element matching the given locator is visible.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the element. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found within the timeout.
        """
        self.info(f"Waiting until element is visible: {locator}")
        self.find_element(locator, timeout=timeout)

    def wait_until_element_is_not_visible(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait until an element matching the given locator is not visible.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the element. If None, use the default timeout.
        :type timeout: float
        """
        self.info(f"Waiting until element is not visible: {locator}")
        if timeout is None:
            timeout = self.ctx.timeout
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                break
            try:
                element = self.find_element(locator, required=False)
                if not element or not element.is_visible():
                    return
            except Exception:
                return
            time.sleep(0.1)

    def wait_until_element_is_enabled(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait until an element matching the given locator is enabled.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the element. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found within the timeout.
        """
        self.info(f"Waiting until element is enabled: {locator}")
        if timeout is None:
            timeout = self.ctx.timeout
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                break
            try:
                element = self.find_element(locator)
                if element.is_enabled():
                    return
            except Exception:
                pass
            time.sleep(0.1)

        raise ElementNotFound(f"Element with locator '{locator}' is not enabled within timeout.")

    def wait_until_element_is_disabled(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait until an element matching the given locator is disabled.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the element. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found within the timeout.
        """
        self.info(f"Waiting until element is disabled: {locator}")
        if timeout is None:
            timeout = self.ctx.timeout
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                break
            try:
                element = self.find_element(locator)
                if not element.is_enabled():
                    return
            except Exception:
                pass
            time.sleep(0.1)

        raise ElementNotFound(f"Element with locator '{locator}' is not disabled within timeout.")

    def wait_until_element_contains_text(self, locator: str, text: str, timeout: Optional[float] = None) -> None:
        """Wait until an element matching the given locator contains the given text.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param text: Text to wait for.
        :type text: str
        :param timeout: Timeout in seconds to wait for the text. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found within the timeout.
        """
        self.info(f"Waiting until element contains text: {locator} contains '{text}'")
        if timeout is None:
            timeout = self.ctx.timeout
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                break
            try:
                element = self.find_element(locator)
                if text in element.window_text():
                    return
            except Exception:
                pass
            time.sleep(0.1)

        raise ElementNotFound(f"Element with locator '{locator}' does not contain text '{text}' within timeout.")

    def wait_until_element_does_not_contain_text(self, locator: str, text: str, timeout: Optional[float] = None) -> None:
        """Wait until an element matching the given locator does not contain the given text.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param text: Text to wait for.
        :type text: str
        :param timeout: Timeout in seconds to wait for the text. If None, use the default timeout.
        :type timeout: float
        """
        self.info(f"Waiting until element does not contain text: {locator} does not contain '{text}'")
        if timeout is None:
            timeout = self.ctx.timeout
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                break
            try:
                element = self.find_element(locator)
                if text not in element.window_text():
                    return
            except Exception:
                return
            time.sleep(0.1)

    def wait_until_window_is_opened(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait until a window matching the given locator is opened.

        :param locator: Locator of the window to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the window. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.WindowNotFound: If the window is not found within the timeout.
        """
        self.info(f"Waiting until window is opened: {locator}")
        self.find_element(locator, timeout=timeout)

    def wait_until_window_is_closed(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait until a window matching the given locator is closed.

        :param locator: Locator of the window to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the window. If None, use the default timeout.
        :type timeout: float
        """
        self.info(f"Waiting until window is closed: {locator}")
        if timeout is None:
            timeout = self.ctx.timeout
        start_time = time.time()

        while True:
            if time.time() - start_time > timeout:
                break
            try:
                self.find_element(locator, required=False)
            except Exception:
                return
            time.sleep(0.1)

    def sleep(self, seconds: float) -> None:
        """Sleep for the given number of seconds.

        :param seconds: Number of seconds to sleep.
        :type seconds: float
        """
        self.info(f"Sleeping for {seconds} seconds")
        time.sleep(seconds)
