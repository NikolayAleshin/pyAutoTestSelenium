# test_login_page.py
import pytest
import allure
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pages.login_page import LoginPage
from fixtures.browser_fixture import browser
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable, wait_and_click

@allure.feature('Login page')
class TestLoginPage:
    @allure.story('Login with valid credentials')
    def test_login_with_valid_credentials(self, browser):
        # Data
        email = 'test@test.com'
        password = 'test123'
        expected_username = 'test test'  # Update with expected username

        # Arrange
        login_page = LoginPage(browser)
        login_page.open()

        # Act
        login_page.click_personal_cabinet()
        login_page.click_entry()
        login_page.login(email, password)
        wait_for_element_visible(browser, login_page.USERNAME_DISPLAY_LOCATOR, timeout=60)

        # Assert
        user_name_element = wait_for_element_visible(browser, login_page.USERNAME_DISPLAY_LOCATOR, timeout=10)
        assert expected_username in user_name_element.text, "Expected username not found in page source."
        allure.step("Validation: Expected username found in page source.")

    @allure.story('Login with invalid credentials')
    def test_login_with_invalid_credentials(self, browser):
        # Data
        email = 'test@test.com'
        password = 'wrongpassword'
        expected_result = 'Неверный e-mail или пароль'

        # Arrange
        login_page = LoginPage(browser)
        login_page.open()

        # Act
        login_page.click_personal_cabinet()
        login_page.click_entry()
        login_page.login(email, password)
        wait_for_element_visible(browser, login_page.ERROR_MESSAGE_LOCATOR, timeout=60)

        # Assert
        assert expected_result in browser.page_source, "Expected text not found in page source."
        allure.step("Validation: Authentication failure message found.")
