from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage
from utils.wait_utils import wait_for_element_visible, wait_for_element_clickable, wait_and_click

class ShoppingCartPage(BasePage):
    SHOPPING_CART_LOCATOR = (By.ID, "rs-cart")
    SHOPPING_CART_ITEMS_LOCATOR = (By.XPATH, "//div[@class='cart-checkout-item rs-cart-item ']")
    SHOPPING_CART_EMPTY_LOCATOR = (By.XPATH, "//h2[contains(text(),'Корзина пуста')]")
    REMOVE_FROM_CART_BUTTON = (By.XPATH, "//a[contains(text(),'Очистить')]")

    def __init__(self, driver):
        super().__init__(driver)
        self.path = '/'

    def click_shopping_cart(self):
        try:
            shopping_cart_button = wait_for_element_visible(self.driver, self.SHOPPING_CART_LOCATOR)
            shopping_cart_button.click()
        except NoSuchElementException:
            print("Shopping cart button is not found on the ShoppingCartPage.")

    def get_shopping_cart_items(self):
        try:
            wait_for_element_visible(self.driver, self.SHOPPING_CART_ITEMS_LOCATOR)
            return self.driver.find_elements(*self.SHOPPING_CART_ITEMS_LOCATOR)
        except NoSuchElementException:
            print("Shopping cart items are not found on the ShoppingCartPage.")
            return []

    def is_shopping_cart_empty(self):
        try:
            empty_cart = wait_for_element_visible(self.driver, self.SHOPPING_CART_EMPTY_LOCATOR)
            return empty_cart
        except NoSuchElementException:
            print("Shopping cart is not empty on the ShoppingCartPage.")
            return None

    def remove_from_cart(self):
        try:
            remove_button = wait_for_element_visible(self.driver, self.REMOVE_FROM_CART_BUTTON)
            remove_button.click()
        except NoSuchElementException:
            print("Remove button is not found on the ShoppingCartPage.")
