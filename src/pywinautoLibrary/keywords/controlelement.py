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
from pywinautoLibrary.errors import ElementNotFound, ElementNotEnabled


class ControlElementKeywords(LibraryComponent):
    """Keywords for interacting with control elements.

    This class contains keywords for interacting with control elements in Windows applications,
    such as buttons, edit boxes, list boxes, etc.
    """

    def click_element(self, locator: str) -> None:
        """Click on an element matching the given locator.

        :param locator: Locator of the element to click.
        :type locator: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        :raises pywinautoLibrary.errors.ElementNotEnabled: If the element is not enabled.
        """
        self.info(f"Clicking element: {locator}")
        element = self.find_element(locator)
        if not element.is_enabled():
            raise ElementNotEnabled(f"Element with locator '{locator}' is not enabled.")
        element.click()

    def double_click_element(self, locator: str) -> None:
        """Double click on an element matching the given locator.

        :param locator: Locator of the element to double click.
        :type locator: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        :raises pywinautoLibrary.errors.ElementNotEnabled: If the element is not enabled.
        """
        self.info(f"Double clicking element: {locator}")
        element = self.find_element(locator)
        if not element.is_enabled():
            raise ElementNotEnabled(f"Element with locator '{locator}' is not enabled.")
        element.double_click()

    def right_click_element(self, locator: str) -> None:
        """Right click on an element matching the given locator.

        :param locator: Locator of the element to right click.
        :type locator: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        """
        self.info(f"Right clicking element: {locator}")
        element = self.find_element(locator)
        element.right_click()

    def get_element_text(self, locator: str) -> str:
        """Get the text of an element matching the given locator.

        :param locator: Locator of the element to get text from.
        :type locator: str
        :return: Text of the element.
        :rtype: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        """
        self.info(f"Getting text from element: {locator}")
        element = self.find_element(locator)
        return element.window_text()

    def set_element_text(self, locator: str, text: str) -> None:
        """Set the text of an element matching the given locator.

        :param locator: Locator of the element to set text to.
        :type locator: str
        :param text: Text to set.
        :type text: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        :raises pywinautoLibrary.errors.ElementNotEnabled: If the element is not enabled.
        """
        self.info(f"Setting text '{text}' to element: {locator}")
        element = self.find_element(locator)
        if not element.is_enabled():
            raise ElementNotEnabled(f"Element with locator '{locator}' is not enabled.")
        element.set_text(text)

    def clear_element_text(self, locator: str) -> None:
        """Clear the text of an element matching the given locator.

        :param locator: Locator of the element to clear text from.
        :type locator: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        :raises pywinautoLibrary.errors.ElementNotEnabled: If the element is not enabled.
        """
        self.info(f"Clearing text from element: {locator}")
        element = self.find_element(locator)
        if not element.is_enabled():
            raise ElementNotEnabled(f"Element with locator '{locator}' is not enabled.")
        element.set_text('')

    def type_into_element(self, locator: str, text: str) -> None:
        """Type text into an element matching the given locator.

        This keyword appends text to the element's current text.

        :param locator: Locator of the element to type into.
        :type locator: str
        :param text: Text to type.
        :type text: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        :raises pywinautoLibrary.errors.ElementNotEnabled: If the element is not enabled.
        """
        self.info(f"Typing text '{text}' into element: {locator}")
        element = self.find_element(locator)
        if not element.is_enabled():
            raise ElementNotEnabled(f"Element with locator '{locator}' is not enabled.")
        element.type_keys(text)

    def is_element_enabled(self, locator: str) -> bool:
        """Check if an element matching the given locator is enabled.

        :param locator: Locator of the element to check.
        :type locator: str
        :return: True if the element is enabled, False otherwise.
        :rtype: bool
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        """
        self.info(f"Checking if element is enabled: {locator}")
        element = self.find_element(locator)
        return element.is_enabled()

    def is_element_visible(self, locator: str) -> bool:
        """Check if an element matching the given locator is visible.

        :param locator: Locator of the element to check.
        :type locator: str
        :return: True if the element is visible, False otherwise.
        :rtype: bool
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        """
        self.info(f"Checking if element is visible: {locator}")
        element = self.find_element(locator)
        return element.is_visible()

    def get_element_attribute(self, locator: str, attribute: str) -> str:
        """Get the value of an attribute from an element matching the given locator.

        :param locator: Locator of the element to get attribute from.
        :type locator: str
        :param attribute: Name of the attribute to get.
        :type attribute: str
        :return: Value of the attribute.
        :rtype: str
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found.
        """
        self.info(f"Getting attribute '{attribute}' from element: {locator}")
        element = self.find_element(locator)
        return element.get_attribute(attribute)

    def wait_for_element(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait for an element matching the given locator to appear.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the element. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found within the timeout.
        """
        self.info(f"Waiting for element: {locator}")
        self.find_element(locator, timeout=timeout)

    def wait_for_element_enabled(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait for an element matching the given locator to be enabled.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the element. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found within the timeout.
        :raises pywinautoLibrary.errors.ElementNotEnabled: If the element is not enabled within the timeout.
        """
        self.info(f"Waiting for element to be enabled: {locator}")
        element = self.find_element(locator, timeout=timeout)
        if not element.is_enabled():
            raise ElementNotEnabled(f"Element with locator '{locator}' is not enabled within timeout.")

    def wait_for_element_visible(self, locator: str, timeout: Optional[float] = None) -> None:
        """Wait for an element matching the given locator to be visible.

        :param locator: Locator of the element to wait for.
        :type locator: str
        :param timeout: Timeout in seconds to wait for the element. If None, use the default timeout.
        :type timeout: float
        :raises pywinautoLibrary.errors.ElementNotFound: If the element is not found within the timeout.
        :raises pywinautoLibrary.errors.ElementNotVisible: If the element is not visible within the timeout.
        """
        self.info(f"Waiting for element to be visible: {locator}")
        element = self.find_element(locator, timeout=timeout)
        if not element.is_visible():
            from pywinautoLibrary.errors import ElementNotVisible
            raise ElementNotVisible(f"Element with locator '{locator}' is not visible within timeout.")
