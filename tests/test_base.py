# -*- coding: utf-8 -*-

#  Licensed under the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License. You may obtain
#  a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#  WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#  License for the specific language governing permissions and limitations
#  under the License.

import unittest
import sys
import os
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from allure_commons.types import AttachmentType

class TestBase(unittest.TestCase):

    def setUp(self):
        self.remote_webdriver_url = os.getenv('REMOTE_WEBDRIVER_URL', 'http://localhost:4444/wd/hub')
        self.build_number = os.getenv('BUILD_NUMBER', None)

        capabilities = DesiredCapabilities.CHROME.copy()
        capabilities['build'] = self.build_number
        self.driver = webdriver.Remote(command_executor=self.remote_webdriver_url, desired_capabilities=capabilities)

        self.driver.maximize_window()
        self.driver.get('https://developers.line.me/en/')

    def tearDown(self):
        if sys.exc_info():
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

        self.driver.quit()
