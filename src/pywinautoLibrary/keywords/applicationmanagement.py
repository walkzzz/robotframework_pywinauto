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

from pywinauto.application import Application

from pywinautoLibrary.base import LibraryComponent
from pywinautoLibrary.errors import ApplicationNotFound


class ApplicationManagementKeywords(LibraryComponent):
    """Keywords for managing Windows applications.

    This class contains keywords for opening, closing, and managing Windows applications.
    """

    def open_application(self, path: str, alias: Optional[str] = None) -> str:
        """Open a new application instance.

        :param path: Path to the application executable.
        :type path: str
        :param alias: Optional alias for the application instance.
        :type alias: str
        :return: Alias of the opened application.
        :rtype: str
        """
        self.info(f"Opening application: {path}")
        app = Application(backend='uia').start(path)
        return self.ctx._apps.register(app, alias)

    def close_application(self, alias: Optional[str] = None) -> None:
        """Close an application instance.

        :param alias: Alias of the application instance to close. If None,
            closes the current application.
        :type alias: str
        """
        self.info(f"Closing application: {alias or 'current'}")
        self.ctx._apps.close(alias)

    def close_all_applications(self) -> None:
        """Close all open application instances.
        """
        self.info("Closing all applications")
        self.ctx._apps.close_all()

    def switch_application(self, alias: str) -> None:
        """Switch to a different application instance.

        :param alias: Alias of the application instance to switch to.
        :type alias: str
        :raises pywinautoLibrary.errors.ApplicationNotFound: If the application alias is not found.
        """
        self.info(f"Switching to application: {alias}")
        try:
            self.ctx._apps.switch(alias)
        except KeyError:
            raise ApplicationNotFound(f"Application with alias '{alias}' not found.")

    def connect_to_application(
        self, process_id: Optional[int] = None,
        path: Optional[str] = None,
        title: Optional[str] = None,
        class_name: Optional[str] = None,
        alias: Optional[str] = None
    ) -> str:
        """Connect to an existing application instance.

        At least one of process_id, path, title, or class_name must be provided.

        :param process_id: Process ID of the application to connect to.
        :type process_id: int
        :param path: Path to the application executable.
        :type path: str
        :param title: Title of the application window.
        :type title: str
        :param class_name: Class name of the application window.
        :type class_name: str
        :param alias: Optional alias for the application instance.
        :type alias: str
        :return: Alias of the connected application.
        :rtype: str
        :raises ValueError: If no connection parameters are provided.
        """
        self.info("Connecting to existing application")
        kwargs = {}
        if process_id:
            kwargs['process'] = process_id
        elif path:
            kwargs['path'] = path
        elif title:
            kwargs['title'] = title
        elif class_name:
            kwargs['class_name'] = class_name
        else:
            raise ValueError("At least one of process_id, path, title, or class_name must be provided.")
        
        app = Application(backend='uia').connect(**kwargs)
        return self.ctx._apps.register(app, alias)

    def is_application_open(self, alias: str) -> bool:
        """Check if an application instance is open.

        :param alias: Alias of the application instance to check.
        :type alias: str
        :return: True if the application is open, False otherwise.
        :rtype: bool
        """
        return alias in self.ctx._apps

    def get_current_application_alias(self) -> Optional[str]:
        """Get the alias of the current application instance.

        :return: Alias of the current application instance.
        :rtype: str
        """
        return self.ctx._apps.current_alias
