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
from typing import Optional

from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn

from pywinautoLibrary.base import LibraryComponent


class ScreenshotKeywords(LibraryComponent):
    """Keywords for taking screenshots.

    This class contains keywords for taking screenshots of windows and elements in Windows applications.
    """

    def capture_screenshot(self, filename: Optional[str] = None) -> str:
        """Capture a screenshot of the current window.

        :param filename: Name of the file to save the screenshot to. If None, a unique name is generated.
        :type filename: str
        :return: Path to the saved screenshot file.
        :rtype: str
        """
        self.info("Capturing screenshot")
        
        # Use PIL to capture screenshot (pywinauto.screenshot might not be available)
        from PIL import ImageGrab
        
        # Get the current active window
        window = self.ctx.app.top_window()
        
        # Get window rectangle and capture
        rect = window.rectangle()
        img = ImageGrab.grab(rect)
        
        # Save the screenshot
        if not filename:
            filename = self._generate_screenshot_filename()
        img.save(filename)
        
        # Log the screenshot
        logger.info(f"Captured screenshot to file: {filename}", html=False)
        logger.info(f"<img src='{filename}' width='800px'>", html=True)
        
        return filename

    def capture_element_screenshot(self, locator: str, filename: Optional[str] = None) -> str:
        """Capture a screenshot of an element matching the given locator.

        :param locator: Locator of the element to capture screenshot from.
        :type locator: str
        :param filename: Name of the file to save the screenshot to. If None, a unique name is generated.
        :type filename: str
        :return: Path to the saved screenshot file.
        :rtype: str
        """
        self.info(f"Capturing screenshot of element: {locator}")
        
        # Use PIL to capture screenshot
        from PIL import ImageGrab
        
        # Find the element
        element = self.find_element(locator)
        
        # Get element rectangle and capture
        rect = element.rectangle()
        img = ImageGrab.grab(rect)
        
        # Save the screenshot
        if not filename:
            filename = self._generate_screenshot_filename()
        img.save(filename)
        
        # Log the screenshot
        logger.info(f"Captured element screenshot to file: {filename}", html=False)
        logger.info(f"<img src='{filename}' width='800px'>", html=True)
        
        return filename

    def _generate_screenshot_filename(self) -> str:
        """Generate a unique filename for a screenshot.

        :return: Generated filename.
        :rtype: str
        """
        import time
        from pathlib import Path
        
        # Get the output directory
        output_dir = BuiltIn().get_variable_value("${OUTPUTDIR}")
        if not output_dir:
            output_dir = os.getcwd()
        
        # Generate a unique filename
        timestamp = time.strftime("%Y%m%d%H%M%S%f")
        filename = f"screenshot_{timestamp}.png"
        filepath = os.path.join(output_dir, filename)
        
        return filepath
    
