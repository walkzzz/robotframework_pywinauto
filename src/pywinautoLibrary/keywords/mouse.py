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

from typing import Optional

from pywinautoLibrary.base import LibraryComponent


class MouseKeywords(LibraryComponent):
    """Keywords for mouse operations.

    This class contains keywords for performing mouse operations in Windows applications,
    such as moving the mouse, clicking, dragging, etc.
    """

    def move_mouse_to_element(self, locator: str, x_offset: int = 0, y_offset: int = 0) -> None:
        """Move the mouse cursor to an element matching the given locator.

        :param locator: Locator of the element to move the mouse to.
        :type locator: str
        :param x_offset: X offset from the center of the element in pixels.
        :type x_offset: int
        :param y_offset: Y offset from the center of the element in pixels.
        :type y_offset: int
        """
        self.info(f"Moving mouse to element: {locator} with offset ({x_offset}, {y_offset})")
        element = self.find_element(locator)
        element.move_mouse_input(coords=(x_offset, y_offset))

    def move_mouse_to_coordinates(self, x: int, y: int) -> None:
        """Move the mouse cursor to the given coordinates.

        :param x: X coordinate to move the mouse to.
        :type x: int
        :param y: Y coordinate to move the mouse to.
        :type y: int
        """
        self.info(f"Moving mouse to coordinates ({x}, {y})")
        from pywinauto.mouse import move
        move((x, y))

    def click_mouse_button(self, button: str = "left", clicks: int = 1, delay: float = 0.0) -> None:
        """Click the mouse button.

        :param button: Mouse button to click (left, right, middle).
        :type button: str
        :param clicks: Number of clicks to perform.
        :type clicks: int
        :param delay: Delay between clicks in seconds.
        :type delay: float
        """
        self.info(f"Clicking mouse button: {button} {clicks} times with delay {delay}s")
        from pywinauto.mouse import click
        click(button=button, clicks=clicks, interval=delay)

    def click_mouse_at_coordinates(self, x: int, y: int, button: str = "left", clicks: int = 1, delay: float = 0.0) -> None:
        """Click the mouse button at the given coordinates.

        :param x: X coordinate to click at.
        :type x: int
        :param y: Y coordinate to click at.
        :type y: int
        :param button: Mouse button to click (left, right, middle).
        :type button: str
        :param clicks: Number of clicks to perform.
        :type clicks: int
        :param delay: Delay between clicks in seconds.
        :type delay: float
        """
        self.info(f"Clicking mouse button: {button} at ({x}, {y}) {clicks} times with delay {delay}s")
        from pywinauto.mouse import click
        click(button=button, coords=(x, y), clicks=clicks, interval=delay)

    def drag_and_drop(self, source_locator: str, target_locator: str) -> None:
        """Drag an element from source to target.

        :param source_locator: Locator of the source element.
        :type source_locator: str
        :param target_locator: Locator of the target element.
        :type target_locator: str
        """
        self.info(f"Dragging from {source_locator} to {target_locator}")
        source = self.find_element(source_locator)
        target = self.find_element(target_locator)
        source.drag_mouse_input(dst=target)

    def drag_and_drop_by_offset(self, locator: str, x_offset: int, y_offset: int) -> None:
        """Drag an element by the given offset.

        :param locator: Locator of the element to drag.
        :type locator: str
        :param x_offset: X offset to drag the element by in pixels.
        :type x_offset: int
        :param y_offset: Y offset to drag the element by in pixels.
        :type y_offset: int
        """
        self.info(f"Dragging element: {locator} by offset ({x_offset}, {y_offset})")
        element = self.find_element(locator)
        element.drag_mouse_input(dst=(x_offset, y_offset))

    def scroll_mouse_wheel(self, locator: str, clicks: int = 1) -> None:
        """Scroll the mouse wheel over an element.

        :param locator: Locator of the element to scroll over.
        :type locator: str
        :param clicks: Number of clicks to scroll. Positive values scroll up, negative values scroll down.
        :type clicks: int
        """
        self.info(f"Scrolling mouse wheel over element: {locator} with {clicks} clicks")
        element = self.find_element(locator)
        element.wheel_mouse_input(delta=clicks)

    def scroll_mouse_wheel_at_coordinates(self, x: int, y: int, clicks: int = 1) -> None:
        """Scroll the mouse wheel at the given coordinates.

        :param x: X coordinate to scroll at.
        :type x: int
        :param y: Y coordinate to scroll at.
        :type y: int
        :param clicks: Number of clicks to scroll. Positive values scroll up, negative values scroll down.
        :type clicks: int
        """
        self.info(f"Scrolling mouse wheel at ({x}, {y}) with {clicks} clicks")
        from pywinauto.mouse import wheel
        wheel(delta=clicks, coords=(x, y))
