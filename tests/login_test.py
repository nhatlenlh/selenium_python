from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest
import time
from selenium.webdriver.support.ui import WebDriverWait
from base_test import BaseTest
from pages.login_page import LoginPage
from utils.read_config import ConfigReader
class TestLogin(BaseTest):

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.enter_username(ConfigReader.get_username())
        login_page.enter_password(ConfigReader.get_password())
        login_page.click_login()

        # dashboard_text = self.driver.find_element(By.XPATH, "//h6[text()='Dashboard']")
        # assert dashboard_text.text == "Dashboard1"
        time.sleep(5)