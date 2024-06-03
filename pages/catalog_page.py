from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible, scroll_into_view, attach_screenshot, wait_for_page_to_load
import allure


class CatalogPage(BasePage):
    CATALOG_LOCATOR = (By.XPATH, "//span[contains(text(),'Каталог')]")
    ELECTRONICS_LOCATOR = (By.XPATH, "//span[contains(text(),'Электроника')]")
    TABLETS_LOCATOR = (
    By.XPATH, "//div[@class='catalog-subcategories re-container-table__inner']//a[contains(text(),'Планшеты')]")
    BREADCRUMB_LOCATOR = (By.XPATH, "//nav[@aria-label='breadcrumb']")
    CARDS_LOCATOR = (By.XPATH, "//div[@class='item-card-container']")
    PRODUCT_SLIDER_LOCATOR = (By.XPATH, "//div[@data-sale-status='show_cost']//div[@class='item-card__inner']")
    PRODUCT_CARDS_LOCATOR_CART = (By.XPATH, "//button[@data-href='/cart/?add=1']")

    def __init__(self, driver):
        super().__init__(driver)
        self.path = '/'

    def click_catalog(self):
        """Click on the catalog link."""
        try:
            catalog_button = wait_for_element_visible(self.driver, self.CATALOG_LOCATOR)
            catalog_button.click()
        except NoSuchElementException:
            print("Catalog button is not found on the CatalogPage.")

    def click_electronics(self):
        """Click on the electronics link."""
        try:
            electronics_button = wait_for_element_visible(self.driver, self.ELECTRONICS_LOCATOR)
            electronics_button.click()
        except NoSuchElementException:
            print("Electronics button is not found on the CatalogPage.")

    def click_tablets(self):
        """Click on the tablets link."""
        try:
            tablets_button = wait_for_element_visible(self.driver, self.TABLETS_LOCATOR)
            tablets_button.click()
        except NoSuchElementException:
            print("Tablets button is not found on the CatalogPage.")

    def click_brand(self, brand_name):
        """Click on the specified brand link."""
        try:
            brand_button = wait_for_element_visible(self.driver, (By.XPATH,
                                                                  f"//div[@class='catalog-subcategories re-container-table__inner']//a[contains(text(),'{brand_name}')]"))
            brand_button.click()
        except NoSuchElementException:
            print(f"Brand {brand_name} is not found on the CatalogPage.")

    @allure.step("Adding a random product to the cart")
    def add_product_to_cart(self):
        try:

            # Locate the product slider element
            scroll_into_view(self.driver, self.PRODUCT_CARDS_LOCATOR_CART)
            add_to_cart_button = wait_for_element_visible(self.driver, self.PRODUCT_CARDS_LOCATOR_CART)
            add_to_cart_button.click()
            attach_screenshot(self.driver, "Product_added_to_cart")

        except NoSuchElementException as e:
            attach_screenshot(self.driver, "NoSuchElementException")
            raise AssertionError("No product cards found or unable to add product to the cart.") from e
