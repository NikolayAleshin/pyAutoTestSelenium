import pytest
import allure
from pages.shopping_cart_page import ShoppingCartPage
from pages.catalog_page import CatalogPage
from fixtures.browser_fixture import browser
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable, wait_and_click, wait_for_page_to_load, scroll_into_view, attach_screenshot

@allure.feature('Shopping Cart page')
class TestShoppingCartPage:
    @allure.story('View shopping cart items')
    def test_view_shopping_cart_items(self, browser):
        expected_items = 1

        product_page = CatalogPage(browser)
        product_page.open('product/Monoblok-Acer-Aspire-Z5763/')

        # # Close any overlays or pop-ups if present
        # try:
        #     overlay_locator = ('xpath', "//button[contains(text(),'Принять')]")
        #     wait_and_click(browser, overlay_locator, timeout=10)
        #     attach_screenshot(browser, "After_closing_overlay")
        # except Exception as e:
        #     allure.step("No overlay found to close.")

        product_page.add_product_to_cart()
        shopping_cart_page = ShoppingCartPage(browser)
        shopping_cart_page.open()

        shopping_cart_page.click_shopping_cart()

        items = shopping_cart_page.get_shopping_cart_items()
        assert len(items) == expected_items, f"Expected {expected_items} items in the shopping cart. Actual: {len(items)}"
        allure.step("Validation: Expected items found in the shopping cart.")

        shopping_cart_page.remove_from_cart()
        shopping_cart_page.click_shopping_cart()
        empty_cart = shopping_cart_page.is_shopping_cart_empty()
        assert "Корзина пуста" in empty_cart.text, f"Expected text not found in page source. Actual: {empty_cart.text}"
        allure.step("Validation: Expected text found in page source.")

    @allure.story('View empty shopping cart')
    def test_view_empty_shopping_cart(self, browser):
        expected_text = 'Корзина пуста'

        shopping_cart_page = ShoppingCartPage(browser)
        shopping_cart_page.open()

        shopping_cart_page.click_shopping_cart()

        empty_cart = shopping_cart_page.is_shopping_cart_empty()
        assert expected_text in empty_cart.text, f"Expected text not found in page source. Actual: {empty_cart.text}"
        allure.step("Validation: Expected text found in page source.")
