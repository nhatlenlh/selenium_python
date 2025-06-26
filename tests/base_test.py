import pytest 
from selenium import webdriver
from selenium.webdriver import Chrome
from time import sleep
from utils.read_config import ConfigReader
class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, request):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(ConfigReader.get_base_url())
        sleep(15)
        request.cls.driver = self.driver
        yield
        self.driver.quit()