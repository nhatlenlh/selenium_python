from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")
time.sleep(2)
hide_btn = driver.find_element(By.XPATH, "//*[@id='hide-textbox']")
show_btn = driver.find_element(By.XPATH, "//*[@id='show-textbox']")
displayed_textbox = driver.find_element(By.XPATH, "//*[@id='displayed-text']")
time.sleep(1)
hide_btn.click()
time.sleep(2)
driver.execute_script("arguments[0].value = 'Hello world'",displayed_textbox)
time.sleep(2)
show_btn.click()
time.sleep(3)






# bmwRadioButton = driver.find_element(By.XPATH, "//*[@id='bmwradio']")
# benzRadioButton = driver.find_element(By.XPATH, "//*[@id='benzradio']")
# hondaRadioButton = driver.find_element(By.XPATH, "//*[@id='hondaradio']")
# time.sleep(1)
# benzRadioButton.click()
# time.sleep(3)
# bmwRadioButton.click()
# time.sleep(2)
        


