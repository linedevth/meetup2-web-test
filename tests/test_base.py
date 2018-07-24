import unittest
import sys
import allure
from selenium import webdriver
from allure_commons.types import AttachmentType


class TestBase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://developers.line.me/en/')

    def tearDown(self):
        if sys.exc_info():
            allure.attach(self.driver.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)

        self.driver.quit()