from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/find_xpath_form"

#link = "http://suninjuly.github.io/simple_form_find_task.html"

number = (str(math.ceil(math.pow(math.pi, math.e)*10000)))

try:
    browser = webdriver.Chrome()
    browser.get(link)

  # link = browser.find_element(By.LINK_TEXT, number)
 #   link.click()

    input1 = browser.find_element(By.NAME, "first_name")
    input1.send_keys("Tamara")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Vash")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Kyiv")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Ukraine")
    button = browser.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
