from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pytest
import time

class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver
        self.menu_vacancies = (By.XPATH, "//a[text() = 'Vacancies']")
        self.add_button = (By.XPATH, "//button[@class = 'oxd-button oxd-button--medium oxd-button--secondary']")
        self.vacancy_name_input = (By.XPATH, "//label[text()='Vacancy Name']/following::input")
        self.job_title_dropdown = (By.XPATH, "//label[text()='Job Title']/following::div[1]")
        self.job_title_option = (By.XPATH, '//div[@role="listbox"]//span[text()="Automation Tester"]')
        self.description_input  = (By.XPATH, "//textarea[@placeholder ='Type description here']")
        self.hiring_manager_input = (By.XPATH, "//input[@placeholder ='Type for hints...']")
        self.num_positions_input = (By.XPATH, '//label[text()="Number of Positions"]/following::input')
        self.save_button = (By.XPATH, "//button[@class = 'oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space']")
    def click_vacancies_tab(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.menu_vacancies)
        ).click()
    def click_add_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_button)
        ).click()
    def add_new_vacancy(self, vacancy_name,description, hiring_manager, num_position):
        self.driver.find_element(*self.vacancy_name_input).send_keys(vacancy_name)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.job_title_dropdown)
        ).click()
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.job_title_option)
        ).click()
        self.driver.find_element(*self.description_input).send_keys(description)
        self.driver.find_element(*self.hiring_manager_input).send_keys(hiring_manager)
        self.driver.find_element(*self.num_positions_input).send_keys(num_position)
        self.driver.find_element(*self.save_button).click()


