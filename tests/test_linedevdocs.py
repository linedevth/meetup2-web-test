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

from tests.test_base import TestBase
from tests.page import MainPage
import allure


class LINEDevDocsTest(TestBase):
    """Another simple test class for LINE Developer MeetUp"""

    @allure.description('LINE Developer Console Page Title Should Be \'Document top\'')
    def test_linedev_docs_page_title(self):
        main_page = MainPage(self.driver)
        document_page = main_page.click_documents_button()
        self.assertEqual(document_page.get_title(), 'Document top', msg='Title is not \'Document top\'')

    @allure.description('LINE Login Documentation Title Should Be \'LINE Login\'')
    def test_linedev_docs_page_contains_line_login(self):
        main_page = MainPage(self.driver)
        document_page = main_page.click_documents_button()
        line_login_doc_page = document_page.click_line_login()
        self.assertEqual(line_login_doc_page.get_title(), 'LINE Login', msg='Title is not \'LINE Login\'')

    @allure.description('LINE Documentation Page Should Contain Menu for LINE Login SDK for iOS App')
    def test_linedev_docs_contains_sdk_for_ios(self):
        main_page = MainPage(self.driver)
        document_page = main_page.click_documents_button()
        self.assertTrue(document_page.should_contains_text('LINE SDK for iOS'))
