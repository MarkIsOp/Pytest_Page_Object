from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import time

links = ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "123abcAeq2"
        link = "http://selenium1py.pythonanywhere.com"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.should_not_be_success_message()
        product_page.add_to_basket()
        product_page.should_be_same_product()
    
    def test_user_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
        product_page = ProductPage(browser, link)
        product_page.open()
        product_page.go_to_basket_page()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.basket_should_be_empty()

def test_promo(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.should_not_be_success_message()
    product_page.add_to_basket()    
    product_page.solve_quiz_and_get_code()
    product_page.should_be_same_product()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()

@pytest.mark.xfail
def test_guest_cant_see_product_in_basket_opened_from_product_page_fail(browser):
    link = "https://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.basket_should_be_empty()


