import math

from selenium import webdriver
from selenium.webdriver.common.by import By



link = "http://suninjuly.github.io/find_link_text"

#link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    print(math.ceil(math.pow(math.pi, math.e)*10000))
