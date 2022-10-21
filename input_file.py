import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("John")

    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("Low")

    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("furgqw@gmail.com")

    input4 = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file_for_input.text')
    input4.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
