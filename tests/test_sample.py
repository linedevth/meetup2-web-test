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

import allure

from tests.page import MainPage
from tests.test_base import TestBase


class MeetUpTestDemo(TestBase):
    """A simple test class for LINE Developer MeetUp"""

    @allure.description('Test LINE Developers Page Load')
    def test_page_load(self):
        """
        Test LINE Developers Page Load
        """
        page = MainPage(self.driver)
        self.assertEqual(page.get_title(), 'LINE Developers', msg="Page Title is not \'LINE Developers\'")

    # @allure.description('Test Login To Developer Console Success')
    # def test_line_login_success(self):
    #     """
    #     Test Login To LINE Developer Website
    #     """
    #     main_page = MainPage(self.driver)
    #     login_page = main_page.click_login_button()
    #     login_page.enter_email('thqaat07@gmail.com')
    #     login_page.enter_password('thqaat1234!')
    #     dev_console_page = login_page.click_login_button()
    #     self.assertIsNotNone(dev_console_page.get_provider_title(), msg='Dev Console Title is None')

    # @allure.description('Test Click Blog URL And Assert Blog Page Title')
    # def test_blog_url(self):
    #     """
    #     Test Click on Blog Link, Then Open A New Tab and Check Page Title
    #     """
    #     main_page = MainPage(self.driver)
    #     blog_page = main_page.click_blog_link()
    #     self.assertEqual(blog_page.get_title(), 'LINE Engineering Blog', msg='Title is not \'LINE Engineering Blog\'')
