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

from tests.base import Page
from tests.locators import *
import allure


class MainPage(Page):
    def __init__(self, driver):
        self.locator = MainPageLocators
        super().__init__(driver)

    @allure.step('Go To Console')
    def click_login_button(self):
        self.find_element(*self.locator.LOGIN).click()
        return LoginPage(self.driver)

    @allure.step('Click On Blog Link')
    def click_blog_link(self):
        self.find_element(*self.locator.BLOG_LINK).click()
        self.switch_to_tab(1)
        return BlogPage(self.driver)

    @allure.step('Switch To Tab')
    def switch_to_tab(self, title_or_index):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[title_or_index])

    @allure.step('Go To Documents')
    def click_documents_button(self):
        self.find_element(*self.locator.DOCUMENT_LINK).click()
        return DocumentPage(self.driver)


class LoginPage(Page):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super().__init__(driver)

    @allure.step('Enter an Email')
    def enter_email(self, email):
        self.find_element(*self.locator.EMAIL).send_keys(email)
        return self

    @allure.step('Enter Password')
    def enter_password(self, password):
        self.find_element(*self.locator.PASSWORD).send_keys(password)
        return self

    @allure.step('Click Login Button')
    def click_login_button(self):
        self.find_element(*self.locator.LOGIN_BUTTON).click()
        return DevConsolePage(self.driver)


class DevConsolePage(Page):
    def __init__(self, driver):
        self.locator = DevConsoleLocators
        super().__init__(driver)

    @allure.step('Get Provider Title')
    def get_provider_title(self):
        return self.get_text(*self.locator.PROVIDER_TITLE).strip()


class BlogPage(Page):
    def __init__(self, driver):
        self.locator = BlogLocators
        super().__init__(driver)


class DocumentPage(Page):
    def __init__(self, driver):
        self.locator = DocumentLocators
        super().__init__(driver)

    @allure.step('Click LINE Login')
    def click_line_login(self):
        self.find_element(*self.locator.LINE_LOGIN_CARD).click()
        return LINELoginDocumentPage(self.driver)


class LINELoginDocumentPage(DocumentPage):
    def __init__(self, driver):
        self.locator = LINELoginDocumentLocators
        super().__init__(driver)