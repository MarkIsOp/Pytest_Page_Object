from .pages.base_page import BasePage
from .pages.product_page import ProductPage
import pytest

links = ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"]

def test_promo(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_basket()
    product_page.solve_quiz_and_get_code()

@pytest.mark.promo
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    product_page = ProductPage(browser, url)
    product_page.open()
    product_page.add_to_basket()    
    product_page.solve_quiz_and_get_code()
    product_page.should_be_same_product()
