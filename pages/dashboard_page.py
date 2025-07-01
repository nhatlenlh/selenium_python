from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.admin_tab = (By.XPATH, "//span[text()='Admin']")
        self.recruitment_tab = (By.XPATH, "//span[text()='Recruitment']")
    def is_admin_tab_visible(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.admin_tab))
    def click_admin_tab(self):
        admin_tab = self.driver.find_element(*self.admin_tab)
        admin_tab.click()
    def click_recruitment_tab(self):
        recruitment_tab = self.driver.find_element(*self.recruitment_tab)
        recruitment_tab.click()