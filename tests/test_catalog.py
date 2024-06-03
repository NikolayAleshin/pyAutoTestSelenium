#test_catalog.py
import pytest
import allure
from pages.catalog_page import CatalogPage
from fixtures.browser_fixture import browser
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable, wait_and_click, wait_for_page_to_load, scroll_into_view, attach_screenshot

@allure.feature('Catalog page')
class TestCatalogPage:
    @allure.story('Select a specific brand in Tablets')
    def test_select_brand_in_tablets(self, browser):
        # Data
        brand_name = 'Digma'
        expected_breadcrumb = 'Главная\nЭлектроника\nПланшеты\nDigma'

        # Arrange
        catalog_page = CatalogPage(browser)
        catalog_page.open()

        # Act
        catalog_page.click_catalog()
        catalog_page.click_electronics()
        wait_for_page_to_load(browser, timeout=90)

        # Debug: Attach screenshot after loading electronics section
        attach_screenshot(browser, "After_loading_electronics_section")

        # Close any overlays or pop-ups if present
        try:
            overlay_locator = ('xpath', "//button[contains(text(),'Принять')]")
            wait_and_click(browser, overlay_locator, timeout=10)
            attach_screenshot(browser, "After_closing_overlay")
        except Exception as e:
            allure.step("No overlay found to close.")

        scroll_into_view(browser, catalog_page.TABLETS_LOCATOR)
        wait_for_element_visible(browser, catalog_page.TABLETS_LOCATOR, timeout=90)

        catalog_page.click_tablets()
        catalog_page.click_brand(brand_name)
        wait_for_element_visible(browser, catalog_page.BREADCRUMB_LOCATOR, timeout=60)

        # Assert
        breadcrumb_element = wait_for_element_visible(browser, catalog_page.BREADCRUMB_LOCATOR, timeout=10)
        actual_breadcrumb = breadcrumb_element.text
        allure.attach(actual_breadcrumb, name="Actual Breadcrumb", attachment_type=allure.attachment_type.TEXT)
        assert expected_breadcrumb in actual_breadcrumb, f"Expected breadcrumb not found in page source. Actual: {actual_breadcrumb}"
        allure.step("Validation: Expected breadcrumb found in page source.")

        catalog_cards = browser.find_elements(*catalog_page.CARDS_LOCATOR)
        assert len(catalog_cards) > 0, "No cards found on the page."
        allure.step("Validation: Cards found on the page.")
