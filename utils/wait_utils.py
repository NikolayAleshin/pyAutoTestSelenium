from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import allure


@allure.step("Waiting for element to be visible: {locator}")
def wait_for_element_visible(driver, locator, timeout=30):
    """Wait for an element to be visible on the page and return it."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(locator))
        # Log element details
        allure.attach(str(element.get_attribute('outerHTML')), name="Element HTML when visible")
        return element
    except (TimeoutException, NoSuchElementException) as e:
        # Take a screenshot before raising the error
        attach_screenshot(driver, "Element not visible")
        raise AssertionError(f"Element {locator} was not visible within {timeout} seconds.") from e


@allure.step("Waiting for element to be clickable: {locator}")
def wait_for_element_clickable(driver, locator, timeout=30):
    """Wait for an element to be clickable and return it."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        # Log element details
        allure.attach(str(element.get_attribute('outerHTML')), name="Element HTML when clickable")
        return element
    except (TimeoutException, NoSuchElementException) as e:
        # Take a screenshot before raising the error
        attach_screenshot(driver, "Element not clickable")
        raise AssertionError(f"Element {locator} was not clickable within {timeout} seconds.") from e


@allure.step("Waiting for element and clicking: {locator}")
def wait_and_click(driver, locator, timeout=30):
    """Wait for an element to be clickable and click it."""
    element = wait_for_element_clickable(driver, locator, timeout)
    element.click()


def attach_screenshot(driver, name):
    """Attach a screenshot to the Allure report."""
    allure.attach(driver.get_screenshot_as_png(), name=name, attachment_type=allure.attachment_type.PNG)


@allure.step("Waiting for page to be fully loaded")
def wait_for_page_to_load(driver, timeout=30):
    """Wait for the page to be fully loaded."""
    try:
        WebDriverWait(driver, timeout).until(
            lambda d: d.execute_script('return document.readyState') == 'complete'
        )
    except TimeoutException:
        attach_screenshot(driver, "Page not fully loaded")
        raise AssertionError(f"Page did not load within {timeout} seconds.")


@allure.step("Scrolling element into view: {locator}")
def scroll_into_view(driver, locator):
    """Scroll the element into view."""
    element = driver.find_element(*locator)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", element)
    # Debug: Attach screenshot after scrolling
    attach_screenshot(driver, "After_scrolling_into_view")