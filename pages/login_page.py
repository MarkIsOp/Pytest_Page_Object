from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import LoginPageLocators
from .locators import MainPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url == self.browser.find_element(*MainPageLocators.LOGIN_LINK).get_attribute('href'), "Currently not in Login Page"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL_FIELD), "Login field is not presented"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASS_FIELD), "Pass field is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL_FIELD), "Login field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1_FIELD), "Pass field is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2_FIELD), "Repeat pass field is not presented"