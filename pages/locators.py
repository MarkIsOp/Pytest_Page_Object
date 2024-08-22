from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=login-username]")
    LOGIN_PASS_FIELD = (By.CSS_SELECTOR, "input[name=login-password]")
    REG_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name=registration-email]")
    REG_PASS1_FIELD = (By.CSS_SELECTOR, "input[name=registration-password1]")
    REG_PASS2_FIELD = (By.CSS_SELECTOR, "input[name=registration-password2]")