from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure

class BasePage:
    def __init__(self, driver, base_url='https://mega.readyscript.ru/'):
        self.driver = driver
        self.base_url = base_url

    def open(self, path=''):
        """Navigate to a specific path relative to the base URL."""
        url = self.base_url + path
        self.driver.get(url)
