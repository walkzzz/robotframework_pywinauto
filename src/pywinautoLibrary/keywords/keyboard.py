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


class KeyboardKeywords(LibraryComponent):
    """Keywords for keyboard operations.

    This class contains keywords for performing keyboard operations in Windows applications,
    such as typing text, pressing keys, etc.
    """

    def type_text(self, text: str, delay: float = 0.0) -> None:
        """Type the given text.

        :param text: Text to type.
        :type text: str
        :param delay: Delay between keystrokes in seconds.
        :type delay: float
        """
        self.info(f"Typing text: '{text}' with delay {delay}s")
        from pywinauto.keyboard import type_keys
        type_keys(text, with_spaces=True, pause=delay)

    def press_keys(self, keys: str, delay: float = 0.0) -> None:
        """Press the given keys.

        :param keys: Keys to press. Use special key names like {ENTER}, {TAB}, {CTRL}, etc.
        :type keys: str
        :param delay: Delay between keystrokes in seconds.
        :type delay: float
        """
        self.info(f"Pressing keys: '{keys}' with delay {delay}s")
        from pywinauto.keyboard import send_keys
        send_keys(keys, pause=delay)

    def press_key_combination(self, *keys: str) -> None:
        """Press a combination of keys.

        :param keys: Keys to press simultaneously. Use special key names like CTRL, SHIFT, ALT, etc.
        :type keys: str
        """
        self.info(f"Pressing key combination: {'+'.join(keys)}")
        from pywinauto.keyboard import send_keys
        key_combination = '+'.join(keys)
        send_keys(key_combination)

    def press_and_release_key(self, key: str, delay: float = 0.0) -> None:
        """Press and release a key.

        :param key: Key to press and release.
        :type key: str
        :param delay: Delay between pressing and releasing the key in seconds.
        :type delay: float
        """
        self.info(f"Pressing and releasing key: '{key}' with delay {delay}s")
        from pywinauto.keyboard import send_keys
        send_keys(f"{{{key} down}}{delay}{{{key} up}}")

    def type_text_into_element(self, locator: str, text: str, delay: float = 0.0) -> None:
        """Type text into an element matching the given locator.

        :param locator: Locator of the element to type into.
        :type locator: str
        :param text: Text to type.
        :type text: str
        :param delay: Delay between keystrokes in seconds.
        :type delay: float
        """
        self.info(f"Typing text: '{text}' into element: {locator} with delay {delay}s")
        element = self.find_element(locator)
        element.type_keys(text, with_spaces=True, pause=delay)

    def press_keys_into_element(self, locator: str, keys: str, delay: float = 0.0) -> None:
        """Press keys into an element matching the given locator.

        :param locator: Locator of the element to press keys into.
        :type locator: str
        :param keys: Keys to press. Use special key names like {ENTER}, {TAB}, {CTRL}, etc.
        :type keys: str
        :param delay: Delay between keystrokes in seconds.
        :type delay: float
        """
        self.info(f"Pressing keys: '{keys}' into element: {locator} with delay {delay}s")
        element = self.find_element(locator)
        element.type_keys(keys, pause=delay)
