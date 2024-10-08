from selenium.webdriver.common.by import By
from .base_page import BasePage
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

    def register_new_user(self, email, password):
        mail = self.browser.find_element(*LoginPageLocators.REG_EMAIL_FIELD)
        mail.send_keys(email)
        pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS2_FIELD)
        pass1.send_keys(password)
        pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS1_FIELD)
        pass2.send_keys(password)
        submit = self.browser.find_element(*LoginPageLocators.REG_SUBMIT)
        submit.click()
