import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "https://SunInJuly.github.io/execute_script.html"

browser = webdriver.Chrome()

try:
    browser.get(link)

    x_element = browser.find_element(By.ID,"input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "[for='robotCheckbox']")
    option1.click()

    button = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("window.scrollBy(0, 100);")

    option2 = browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']")
    option2.click()

    button.click()


finally:
    time.sleep(30)
    browser.quit()
