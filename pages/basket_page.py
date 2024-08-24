from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_should_be_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_QUANTITY), \
            "basket is not empty"
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY), \
            "message 'basket is empty' is not present"
