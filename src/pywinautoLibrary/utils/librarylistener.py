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


class LibraryListener:
    """Library listener for Robot Framework events.

    This class implements the Robot Framework listener interface to listen for
    various events during test execution.
    """

    ROBOT_LISTENER_API_VERSION = 2

    def __init__(self):
        """Initialize the library listener."""
        self.ROBOT_LIBRARY_LISTENER = self

    def start_keyword(self, name, attrs):
        """Called when a keyword starts.

        :param name: Name of the keyword.
        :type name: str
        :param attrs: Dictionary containing keyword attributes.
        :type attrs: dict
        """
        pass

    def end_keyword(self, name, attrs):
        """Called when a keyword ends.

        :param name: Name of the keyword.
        :type name: str
        :param attrs: Dictionary containing keyword attributes.
        :type attrs: dict
        """
        pass

    def start_test(self, name, attrs):
        """Called when a test starts.

        :param name: Name of the test.
        :type name: str
        :param attrs: Dictionary containing test attributes.
        :type attrs: dict
        """
        pass

    def end_test(self, name, attrs):
        """Called when a test ends.

        :param name: Name of the test.
        :type name: str
        :param attrs: Dictionary containing test attributes.
        :type attrs: dict
        """
        pass

    def start_suite(self, name, attrs):
        """Called when a suite starts.

        :param name: Name of the suite.
        :type name: str
        :param attrs: Dictionary containing suite attributes.
        :type attrs: dict
        """
        pass

    def end_suite(self, name, attrs):
        """Called when a suite ends.

        :param name: Name of the suite.
        :type name: str
        :param attrs: Dictionary containing suite attributes.
        :type attrs: dict
        """
        pass

    def output_file(self, path):
        """Called when an output file is created.

        :param path: Path to the output file.
        :type path: str
        """
        pass

    def log_message(self, message):
        """Called when a log message is generated.

        :param message: Dictionary containing log message attributes.
        :type message: dict
        """
        pass

    def message(self, message):
        """Called when a message is generated.

        :param message: Dictionary containing message attributes.
        :type message: dict
        """
        pass
