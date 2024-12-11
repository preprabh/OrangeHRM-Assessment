import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from config import variables


class LoginPage:
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

    def login(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        time.sleep(4)

        driver.find_element(By.NAME, "username").send_keys(variables.username)
        driver.find_element(By.NAME, "password").send_keys(variables.password)

        driver.find_element(By.TAG_NAME, "button").click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(expected_conditions.presence_of_element_located((By.TAG_NAME, "h6")))

        assert "Dashboard" in element.text

        return driver
