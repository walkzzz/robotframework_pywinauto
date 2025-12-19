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

import os
from datetime import timedelta
from typing import Optional, Union

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn, RobotNotRunningError

from .context import ContextAware
from ..utils import is_noney, _convert_timeout


class LibraryComponent(ContextAware):
    def info(self, msg: str, html: bool = False):
        """Log a message with INFO level.

        :param msg: Message to log.
        :type msg: str
        :param html: If True, the message is interpreted as HTML.
        :type html: bool
        """
        logger.info(msg, html)

    def debug(self, msg: str, html: bool = False):
        """Log a message with DEBUG level.

        :param msg: Message to log.
        :type msg: str
        :param html: If True, the message is interpreted as HTML.
        :type html: bool
        """
        logger.debug(msg, html)

    def log(self, msg: str, level: str = "INFO", html: bool = False):
        """Log a message with the given level.

        :param msg: Message to log.
        :type msg: str
        :param level: Log level (INFO, DEBUG, WARN, ERROR).
        :type level: str
        :param html: If True, the message is interpreted as HTML.
        :type html: bool
        """
        if not is_noney(level):
            logger.write(msg, level.upper(), html)

    def warn(self, msg: str, html: bool = False):
        """Log a message with WARN level.

        :param msg: Message to log.
        :type msg: str
        :param html: If True, the message is interpreted as HTML.
        :type html: bool
        """
        logger.warn(msg, html)

    def assert_window_contains(
        self,
        locator: str,
        control_type: Optional[str] = None,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        """Assert that current window contains the given element.

        :param locator: Locator of the element to check.
        :type locator: str
        :param control_type: Type of the control to check.
        :type control_type: str
        :param message: Custom error message if assertion fails.
        :type message: str
        :param loglevel: Log level to use when logging the source.
        :type loglevel: str
        :raises AssertionError: If the element is not found.
        """
        control_message = control_type or "element"
        if not self.find_element(locator, control_type, required=False):
            if message is None:
                message = (
                    f"Window should have contained {control_message} '{locator}' but did not."
                )
            raise AssertionError(message)
        logger.info(f"Current window contains {control_message} '{locator}'.")

    def assert_window_not_contains(
        self,
        locator: str,
        control_type: Optional[str] = None,
        message: Optional[str] = None,
        loglevel: str = "TRACE",
    ):
        """Assert that current window does not contain the given element.

        :param locator: Locator of the element to check.
        :type locator: str
        :param control_type: Type of the control to check.
        :type control_type: str
        :param message: Custom error message if assertion fails.
        :type message: str
        :param loglevel: Log level to use when logging the source.
        :type loglevel: str
        :raises AssertionError: If the element is found.
        """
        control_message = control_type or "element"
        if self.find_element(locator, control_type, required=False):
            if message is None:
                message = f"Window should not have contained {control_message} '{locator}'."
            raise AssertionError(message)
        logger.info(f"Current window does not contain {control_message} '{locator}'.")

    def get_timeout(self, timeout: Union[str, int, timedelta, None] = None) -> float:
        """Get timeout value in seconds.

        :param timeout: Timeout value in seconds or Robot Framework time format.
        :type timeout: str, int, timedelta, or None
        :return: Timeout value in seconds.
        :rtype: float
        """
        if timeout is None:
            return self.ctx.timeout
        return _convert_timeout(timeout)

    @property
    def log_dir(self):
        """Get the directory where log files are written.

        :return: Path to the log directory.
        :rtype: str
        """
        try:
            logfile = BuiltIn().get_variable_value("${LOG FILE}")
            if logfile == "NONE":
                return BuiltIn().get_variable_value("${OUTPUTDIR}")
            return os.path.dirname(logfile)
        except RobotNotRunningError:
            return os.getcwd()
