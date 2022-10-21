import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()

def sum(x, y):
    return str(x + y)

try:
    browser.get(link)

    x = int(browser.find_element(By.ID, "num1").text)

    y = int(browser.find_element(By.ID, "num2").text)

    summary = sum(x, y)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(summary)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(30)
    browser.quit()
