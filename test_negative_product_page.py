from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import pytest

link = "https://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.should_not_be_success_message(), "Success message is not presented"

def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message(), "Success message is not presented"

def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.success_message_should_disappear(), "Success message did not dissapear"