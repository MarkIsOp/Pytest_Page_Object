from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=login-username]")
    LOGIN_PASS_FIELD = (By.CSS_SELECTOR, "input[name=login-password]")

    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=registration-email]")
    REG_PASS1_FIELD = (By.CSS_SELECTOR, "input[name=registration-password1]")
    REG_PASS2_FIELD = (By.CSS_SELECTOR, "input[name=registration-password2]")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")

    ACTUAL_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main > p:nth-child(2)")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alert-info > .alertinner > p > strong")
    
    NAME_OF_PRODUCT = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    WHAT_ADDED = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success:nth-child(1) > .alertinner > strong")