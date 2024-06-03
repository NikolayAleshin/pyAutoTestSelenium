from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable, wait_and_click

class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-auth1")
    PASSWORD_INPUT = (By.ID, "input-auth2")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and contains(@class, 'btn-primary')]")
    PERSONAL_CABINET_BUTTON = (By.XPATH, "//span[contains(text(),'Личный кабинет')]")
    USERNAME_DISPLAY_LOCATOR = (By.XPATH, "//a[@href='/my/']//span[@class='ms-2']")
    ERROR_MESSAGE_LOCATOR = (By.CSS_SELECTOR, "div.invalid-feedback")
    BUTTON_ENTRY = (By.XPATH, "//a[contains(text(),'Вход')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.path = '/'

    def enter_username(self, username):
        """Enter username into the username field."""
        try:
            username_field = wait_for_element_visible(self.driver, self.USERNAME_INPUT)
            username_field.clear()
            username_field.send_keys(username)
        except NoSuchElementException:
            print("Username field is not found on the LoginPage.")

    def enter_password(self, password):
        """Enter password into the password field."""
        try:
            password_field = wait_for_element_visible(self.driver, self.PASSWORD_INPUT)
            password_field.clear()
            password_field.send_keys(password)
        except NoSuchElementException:
            print("Password field is not found on the LoginPage.")

    def submit(self):
        """Submit the login form."""
        try:
            wait_and_click(self.driver, self.LOGIN_BUTTON)
        except NoSuchElementException:
            print("Login button is not found on the LoginPage.")

    def click_personal_cabinet(self):
        """Click on the personal cabinet link."""
        try:
            wait_and_click(self.driver, self.PERSONAL_CABINET_BUTTON)
        except NoSuchElementException:
            print("Personal cabinet button is not found on the LoginPage.")

    def click_entry(self):
        """Click on the entry button."""
        try:
            wait_and_click(self.driver, self.BUTTON_ENTRY)
        except NoSuchElementException:
            print("Entry button is not found on the LoginPage.")

    def login(self, username, password):
        """Perform a complete login action using username and password."""
        self.enter_username(username)
        self.enter_password(password)
        self.submit()
