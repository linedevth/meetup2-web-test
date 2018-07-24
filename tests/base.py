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

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException


class Page(object):

    def __init__(self, driver, base_url='https://developers.line.me/en/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(self.driver, self.timeout, poll_frequency=2, ignored_exceptions=[NoSuchElementException])

    def find_element(self, *locator):
        self.wait.until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)

    def get_text(self, *locator):
        return self.find_element(*locator).text

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def should_contains_text(self, text):
        return text in self.driver.page_source
