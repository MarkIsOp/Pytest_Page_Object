from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_cart.click()

    def should_be_same_product(self):
        price1 = self.browser.find_element(*ProductPageLocators.ACTUAL_PRICE).text
        price2 = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        name1 = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name2 = self.browser.find_element(*ProductPageLocators.WHAT_ADDED).text
        assert price1 == price2, f"prices are not the same, {price1}, {price2}"
        assert name1 == name2, f"items are not the same, {name1}, {name2}"
