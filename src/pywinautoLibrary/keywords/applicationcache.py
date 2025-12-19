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


class ApplicationCache:
    """Cache for managing multiple application instances.

    This class is responsible for storing and managing multiple instances
    of pywinauto Application objects. It allows registering applications
    with aliases, switching between them, and closing them.
    """

    def __init__(self):
        """Initialize the application cache.

        Creates an empty cache and sets the current application to None.
        """
        self._apps = {}
        self._current = None

    def register(self, app, alias=None):
        """Register a new application instance.

        :param app: The pywinauto Application instance to register.
        :type app: pywinauto.application.Application
        :param alias: Alias for the application instance.
        :type alias: str
        :return: The alias used for the application.
        :rtype: str
        """
        if alias is None:
            alias = str(len(self._apps) + 1)
        self._apps[alias] = app
        if self._current is None:
            self._current = alias
        return alias

    def switch(self, alias):
        """Switch to a different application instance.

        :param alias: Alias of the application instance to switch to.
        :type alias: str
        :raises KeyError: If the alias is not found in the cache.
        """
        if alias not in self._apps:
            raise KeyError(f"Application with alias '{alias}' not found.")
        self._current = alias

    def close(self, alias=None):
        """Close an application instance.

        :param alias: Alias of the application instance to close. If None,
            closes the current application.
        :type alias: str or None
        :raises KeyError: If the alias is not found in the cache.
        """
        if alias is None:
            alias = self._current
        if alias not in self._apps:
            raise KeyError(f"Application with alias '{alias}' not found.")
        app = self._apps[alias]
        try:
            app.kill()
        except Exception:
            pass
        del self._apps[alias]
        if self._current == alias:
            self._current = next(iter(self._apps.keys()), None)

    def close_all(self):
        """Close all registered application instances.

        Closes all applications in the cache and clears the cache.
        """
        for alias in list(self._apps.keys()):
            self.close(alias)
        self._apps.clear()
        self._current = None

    @property
    def current(self):
        """Get the current application instance.

        :return: The current pywinauto Application instance.
        :rtype: pywinauto.application.Application or None
        """
        if self._current is None:
            return None
        return self._apps[self._current]

    @property
    def current_alias(self):
        """Get the alias of the current application instance.

        :return: The alias of the current application.
        :rtype: str or None
        """
        return self._current

    @property
    def apps(self):
        """Get all registered application instances.

        :return: Dictionary of registered applications.
        :rtype: dict
        """
        return self._apps.copy()

    def __contains__(self, alias):
        """Check if an alias is in the cache.

        :param alias: Alias to check.
        :type alias: str
        :return: True if the alias is in the cache, False otherwise.
        :rtype: bool
        """
        return alias in self._apps

    def __len__(self):
        """Get the number of registered applications.

        :return: Number of registered applications.
        :rtype: int
        """
        return len(self._apps)
