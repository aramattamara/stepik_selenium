import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestAbs(unittest.TestCase):
    def test_registration1(self):
        self.link = "http://suninjuly.github.io/registration1.html"
        self.__common_test("unlucky_1")

    def test_registration2(self):
        self.link = 'http://suninjuly.github.io/registration2.html'
        self.__common_test("unlucky_2")

    def __common_test(self, expected_message):
        self.browser = webdriver.Chrome()
        self.browser.get(self.link)
        first_name = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_name.send_keys("James")
        last_name = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        last_name.send_keys("Brook")
        email = self.browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email.send_keys("test@gmail.com")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEquals("Congratulations! You have successfully registered!", welcome_text, expected_message)


if __name__ == "__main__":
    unittest.main()
