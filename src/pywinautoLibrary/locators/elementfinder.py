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

from typing import Optional, List, Any
import time

from pywinautoLibrary.errors import ElementNotFound


class ElementFinder:
    """Element finder for locating elements in Windows applications.

    This class is responsible for finding elements in Windows applications
    using various locator strategies.
    """

    def __init__(self, ctx):
        """Initialize the element finder.

        :param ctx: The library context.
        :type ctx: pywinautoLibrary.pywinautoLibrary
        """
        self.ctx = ctx

    def find(
        self,
        locator: str,
        control_type: Optional[str] = None,
        first_only: bool = True,
        required: bool = True,
        parent: Any = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Find element(s) matching the given locator.

        :param locator: Locator to use when searching the element.
        :type locator: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :param first_only: If True, return only the first matching element.
        :type first_only: bool
        :param required: Raise ElementNotFound if element not found when True.
        :type required: bool
        :param parent: Optional parent element to search child elements from.
        :type parent: Any
        :param timeout: Timeout in seconds to wait for the element to appear.
        :type timeout: float
        :return: Found element(s) or None if not found and required is False.
        :rtype: Any or list
        :raises pywinautoLibrary.errors.ElementNotFound: If element not found and required is True.
        """
        if timeout is None:
            timeout = self.ctx.timeout
        start_time = time.time()

        while True:
            try:
                elements = self._find_elements(locator, control_type, first_only, parent)
                if elements:
                    return elements[0] if first_only else elements
            except Exception:
                pass

            if time.time() - start_time > timeout:
                break
            time.sleep(0.1)

        if required:
            raise ElementNotFound(f"Element with locator '{locator}' not found.")
        return None if first_only else []

    def _find_elements(
        self,
        locator: str,
        control_type: Optional[str] = None,
        first_only: bool = True,
        parent: Any = None,
    ) -> List[Any]:
        """Internal method to find elements.

        :param locator: Locator to use when searching the element.
        :type locator: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :param first_only: If True, return only the first matching element.
        :type first_only: bool
        :param parent: Optional parent element to search child elements from.
        :type parent: Any
        :return: List of found elements.
        :rtype: list
        """
        # Parse locator to get strategy and value
        strategy, value = self._parse_locator(locator)
        
        # Determine the root element to search from
        root = parent or self._get_root_element()
        
        # Find elements based on strategy
        elements = self._find_by_strategy(root, strategy, value, control_type)
        
        return elements[:1] if first_only else elements

    def _parse_locator(self, locator: str) -> tuple:
        """Parse locator string to get strategy and value.

        :param locator: Locator string to parse.
        :type locator: str
        :return: Tuple containing strategy and value.
        :rtype: tuple
        """
        # Check for explicit strategy
        strategy_separators = [":", "="]
        for sep in strategy_separators:
            if sep in locator:
                strategy, value = locator.split(sep, 1)
                return strategy.strip().lower(), value.strip()
        
        # Default strategy: auto_id, control_id, text
        return "default", locator.strip()

    def _get_root_element(self) -> Any:
        """Get the root element to start searching from.

        :return: Root element.
        :rtype: Any
        """
        # For now, use the current active window
        return self.ctx.app.top_window()

    def _find_by_strategy(
        self,
        root: Any,
        strategy: str,
        value: str,
        control_type: Optional[str] = None,
    ) -> List[Any]:
        """Find elements based on the given strategy.

        :param root: Root element to search from.
        :type root: Any
        :param strategy: Locator strategy to use.
        :type strategy: str
        :param value: Locator value.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        strategies = {
            "title": self._find_by_title,
            "class": self._find_by_class,
            "control_id": self._find_by_control_id,
            "auto_id": self._find_by_auto_id,
            "text": self._find_by_text,
            "xpath": self._find_by_xpath,
            "default": self._find_by_default,
        }

        finder = strategies.get(strategy, self._find_by_default)
        return finder(root, value, control_type)

    def _find_by_title(
        self, root: Any, value: str, control_type: Optional[str] = None
    ) -> List[Any]:
        """Find elements by title.

        :param root: Root element to search from.
        :type root: Any
        :param value: Title value to match.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        try:
            # For window elements, use window title
            if hasattr(self.ctx.app, 'windows'):
                # Search for windows with the given title
                windows = self.ctx.app.windows(title_re=value)
                if windows:
                    return windows
                # If no exact match, try finding all windows and check manually
                all_windows = self.ctx.app.windows()
                for window in all_windows:
                    try:
                        if value in window.window_text():
                            return [window]
                    except Exception:
                        continue
            return []
        except Exception as e:
            print(f"Error in _find_by_title: {e}")
            return []

    def _find_by_class(
        self, root: Any, value: str, control_type: Optional[str] = None
    ) -> List[Any]:
        """Find elements by class name.

        :param root: Root element to search from.
        :type root: Any
        :param value: Class name to match.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        try:
            if root == self.ctx.app.top_window():
                # Search for windows with the given class name
                windows = self.ctx.app.windows(class_name=value)
                return windows
            else:
                # Search for child elements with the given class name
                elements = root.children(class_name=value)
                return elements
        except Exception:
            return []

    def _find_by_control_id(
        self, root: Any, value: str, control_type: Optional[str] = None
    ) -> List[Any]:
        """Find elements by control ID.

        :param root: Root element to search from.
        :type root: Any
        :param value: Control ID to match.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        try:
            # Convert control ID to integer if possible
            try:
                control_id = int(value)
            except ValueError:
                control_id = value
            
            elements = root.children(control_id=control_id)
            return elements
        except Exception:
            return []

    def _find_by_auto_id(
        self, root: Any, value: str, control_type: Optional[str] = None
    ) -> List[Any]:
        """Find elements by automation ID.

        :param root: Root element to search from.
        :type root: Any
        :param value: Automation ID to match.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        try:
            elements = root.children(auto_id=value)
            return elements
        except Exception:
            return []

    def _find_by_text(
        self, root: Any, value: str, control_type: Optional[str] = None
    ) -> List[Any]:
        """Find elements by text.

        :param root: Root element to search from.
        :type root: Any
        :param value: Text to match.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        try:
            elements = root.children(title_re=value)
            return elements
        except Exception:
            return []

    def _find_by_xpath(
        self, root: Any, value: str, control_type: Optional[str] = None
    ) -> List[Any]:
        """Find elements by XPath.

        :param root: Root element to search from.
        :type root: Any
        :param value: XPath expression.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        try:
            # pywinauto doesn't support XPath directly, but we can use its own backend
            # For now, we'll just return an empty list
            return []
        except Exception:
            return []

    def _find_by_default(
        self, root: Any, value: str, control_type: Optional[str] = None
    ) -> List[Any]:
        """Find elements using the default strategy.

        Default strategy tries to find elements by auto_id, control_id, or text in that order.

        :param root: Root element to search from.
        :type root: Any
        :param value: Value to match.
        :type value: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :return: List of found elements.
        :rtype: list
        """
        # Try auto_id first
        elements = self._find_by_auto_id(root, value, control_type)
        if elements:
            return elements
        
        # Try control_id next
        elements = self._find_by_control_id(root, value, control_type)
        if elements:
            return elements
        
        # Try text last
        elements = self._find_by_text(root, value, control_type)
        return elements
