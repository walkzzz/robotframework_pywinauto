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

from datetime import timedelta
from typing import Optional, List, Union

from robot.api import logger
from robot.errors import DataError
from robot.libraries.BuiltIn import BuiltIn
from robot.utils.importer import Importer

from .base import LibraryComponent
from .errors import NoOpenApplication, PluginError
from .keywords import (
    ApplicationManagementKeywords,
    WindowManagementKeywords,
    ControlElementKeywords,
    MouseKeywords,
    KeyboardKeywords,
    WaitingKeywords,
    ScreenshotKeywords,
    ApplicationCache,
)
from .locators import ElementFinder
from .utils import (
    LibraryListener, 
    is_truthy, 
    _convert_timeout, 
    _convert_delay,
    DynamicCore
)


__version__ = "0.1.0"


class pywinautoLibrary(DynamicCore):
    """PywinautoLibrary is a Windows desktop application testing library for Robot Framework.
    """

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(
        self,
        timeout=timedelta(seconds=5),
        run_on_failure="Capture Screenshot",
        screenshot_root_directory: Optional[str] = None,
        plugins: Optional[str] = None,
    ):
        """PywinautoLibrary can be imported with several optional arguments.
        """
        self.timeout = _convert_timeout(timeout)
        self.run_on_failure_keyword = run_on_failure
        self._running_on_failure_keyword = False
        self.screenshot_root_directory = screenshot_root_directory
        self._resolve_screenshot_root_directory()
        self._element_finder = ElementFinder(self)
        self._plugin_keywords = []
        libraries = [
            ApplicationManagementKeywords(self),
            WindowManagementKeywords(self),
            ControlElementKeywords(self),
            MouseKeywords(self),
            KeyboardKeywords(self),
            WaitingKeywords(self),
            ScreenshotKeywords(self),
        ]
        self.ROBOT_LIBRARY_LISTENER = LibraryListener()
        self._running_keyword = None
        self._plugins = []
        if is_truthy(plugins):
            plugin_libs = self._parse_plugins(plugins)
            self._plugins = plugin_libs
            libraries = libraries + plugin_libs
        self._apps = ApplicationCache()
        DynamicCore.__init__(self, libraries)

    @property
    def app(self):
        """Current active application.
        """
        if not self._apps.current:
            raise NoOpenApplication("No application is open.")
        return self._apps.current

    def run_keyword(self, name: str, args: tuple, kwargs: dict):
        """Run keyword with the given name and arguments.
        """
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except Exception:
            self.failure_occurred()
            raise

    def failure_occurred(self):
        """Method that is executed when a PywinautoLibrary keyword fails.
        """
        if self._running_on_failure_keyword or not self.run_on_failure_keyword:
            return
        try:
            self._running_on_failure_keyword = True
            if self.run_on_failure_keyword.lower() == "capture screenshot":
                # Use run_keyword to execute the screenshot keyword
                self.run_keyword("capture_screenshot", (), {})
            else:
                BuiltIn().run_keyword(self.run_on_failure_keyword)
        except Exception as err:
            logger.warn(
                f"Keyword '{self.run_on_failure_keyword}' could not be run on failure: {err}"
            )
        finally:
            self._running_on_failure_keyword = False

    def _resolve_screenshot_root_directory(self):
        """Resolve the screenshot root directory.
        """
        if not self.screenshot_root_directory:
            return
        # No special handling needed for now

    def _parse_plugins(self, plugins):
        """Parse plugin configuration and return plugin instances.
        """
        libraries = []
        importer = Importer("test library")
        for plugin in plugins.split(","):
            plugin = plugin.strip()
            plugin_and_args = plugin.split(";")
            plugin_name = plugin_and_args[0]
            plugin_args = plugin_and_args[1].split(":") if len(plugin_and_args) > 1 else []
            try:
                plugin_class = importer.import_class_or_module(plugin_name)
                plugin_instance = plugin_class(self, *plugin_args)
                libraries.append(plugin_instance)
            except Exception as e:
                raise PluginError(f"Failed to import plugin '{plugin_name}': {e}")
        return libraries
