from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


try:

    browser = webdriver.Chrome()
    browser.get(link1)

    first_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
    first_name.send_keys("James")

    last_name = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    last_name.send_keys("Brook")

    email = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
    email.send_keys("test@gmail.com")


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
