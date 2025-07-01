from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.XPATH, "//div[@class = 'oxd-topbar-header-title']")
        self.username_field = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.employee_name_field = (By.XPATH, "//input[@placeholder='Type for hints...']")
        self.add_button = (By.XPATH, "//button[@class = 'oxd-button oxd-button--medium oxd-button--secondary']")
        self.user_role_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[1]")
        self.status_dropdown = (By.XPATH, "(//div[@class='oxd-select-text-input'])[2]")
        self.new_username = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[2]")
        self.password_field = (By.XPATH, "(//input[@type='password'])[1]")
        self.confirm_password = (By.XPATH, "(//input[@type='password'])[2]")
        self.save_button = (By.XPATH, "//button[@type='submit']")
        self.search_input = (By.XPATH, "(//label[text()='Username']/following::input[1])")
        self.search_button = (By.XPATH, "//button[@class ='oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")

    def is_admin_page(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.page_title)
        )
    def select_dropdown_option(self, dropdown_locator, option_text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator)
        ).click()

        option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@role='option']//span[text()='{option_text}']"))
        )
        option.click()
    def add_new_user(self, employee_name, username, password, role , status):
        self.driver.find_element(*self.add_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(self.employee_name_field)
        )
        self.select_dropdown_option(self.user_role_dropdown, role)
        self.select_dropdown_option(self.status_dropdown, status)

        self.driver.find_element(*self.employee_name_field).send_keys(employee_name)
        suggestion = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located((By.XPATH, f"//div[@role='listbox']//span[contains(text(), '{employee_name}')]"))
        )
        suggestion.click()
        self.driver.find_element(*self.new_username).send_keys(username)
        self.driver.find_element(*self.password_field).send_keys(password)
        self.driver.find_element(*self.confirm_password).send_keys(password)
        time.sleep(2)
        self.driver.find_element(*self.save_button).click()
        WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(self.search_input)
    )

    def search_user(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.search_input)
        ).send_keys(username)
        self.driver.find_element(*self.search_button).click()
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,f"//div[@class='oxd-table-card']//div[contains(text(), '{username}')]"))
        )