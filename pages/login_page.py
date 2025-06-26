from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import time
class LoginPage:
    def __init__(self,driver):
        self.timeout = 10
        self.driver = driver
        self.username_input = (By.XPATH, '//input[@name="username"]')
        self.password_input = (By.XPATH, '//input[@name="password"]')
        self.login_button = (By.XPATH, '//button[@type="submit"]')
    def enter_username(self, username: str):
        user_input =WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.username_input)
        )
        user_input.send_keys(username)
    def enter_password(self, password: str):
         WebDriverWait(self.driver, 10).until(
            lambda d: d.find_element(*self.password_input)
        ).send_keys(password)
    def click_login(self):
        self.driver.find_element(*self.login_button).click()