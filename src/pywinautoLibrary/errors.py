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


class PywinautoLibraryError(Exception):
    """Base exception for PywinautoLibrary errors."""
    pass


class ApplicationNotFound(PywinautoLibraryError):
    """Raised when an application cannot be found."""
    pass


class WindowNotFound(PywinautoLibraryError):
    """Raised when a window cannot be found."""
    pass


class ElementNotFound(PywinautoLibraryError):
    """Raised when an element cannot be found."""
    pass


class ElementNotEnabled(PywinautoLibraryError):
    """Raised when an element is not enabled."""
    pass


class ElementNotVisible(PywinautoLibraryError):
    """Raised when an element is not visible."""
    pass


class NoOpenApplication(PywinautoLibraryError):
    """Raised when no application is open."""
    pass


class PluginError(PywinautoLibraryError):
    """Raised when there is an error with a plugin."""
    pass
