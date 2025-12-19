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


class ContextAware:
    def __init__(self, ctx):
        """Base class exposing attributes from the common context.

        :param ctx: The library itself as a context object.
        :type ctx: pywinautoLibrary.pywinautoLibrary
        """
        self.ctx = ctx

    @property
    def app(self):
        """Current active application.

        :return: Instance of the pywinauto Application.
        :rtype: pywinauto.application.Application
        """
        return self.ctx.app

    @property
    def apps(self):
        """All opened applications.

        :return: Dictionary of opened applications.
        :rtype: dict
        """
        return self.ctx._apps

    @property
    def element_finder(self):
        """Element finder instance.

        :return: Instance of the ElementFinder.
        :rtype: pywinautoLibrary.locators.elementfinder.ElementFinder
        """
        return self.ctx._element_finder

    @element_finder.setter
    def element_finder(self, value: Any):
        """Set element finder instance.

        :param value: Instance of the ElementFinder.
        :type value: pywinautoLibrary.locators.elementfinder.ElementFinder
        """
        self.ctx._element_finder = value

    def find_element(
        self,
        locator: str,
        control_type: Optional[str] = None,
        required: bool = True,
        parent: Any = None,
        timeout: Optional[float] = None,
    ) -> Any:
        """Find element matching `locator`.

        :param locator: Locator to use when searching the element.
            See library documentation for the supported locator syntax.
        :type locator: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :param required: Raise `ElementNotFound` if element not found when
            true, return `None` otherwise.
        :type required: bool
        :param parent: Optional parent element to search child elements
            from. By default, search starts from the root window.
        :type parent: Any
        :param timeout: Timeout in seconds to wait for the element.
        :type timeout: float
        :return: Found element or `None` if element not found and
            `required` is false.
        :rtype: Any
        :raises pywinautoLibrary.errors.ElementNotFound: If element not found
            and `required` is true.
        """
        return self.element_finder.find(locator, control_type, True, required, parent, timeout)

    def find_elements(
        self,
        locator: str,
        control_type: Optional[str] = None,
        parent: Any = None,
    ) -> List[Any]:
        """Find all elements matching `locator`.

        :param locator: Locator to use when searching the element.
            See library documentation for the supported locator syntax.
        :type locator: str
        :param control_type: Limit searching only to these control types.
        :type control_type: str
        :param parent: Optional parent element to search child elements
            from. By default, search starts from the root window.
        :type parent: Any
        :return: list of found elements or empty if elements are not found.
        :rtype: list
        """
        return self.element_finder.find(locator, control_type, False, False, parent)
