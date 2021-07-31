from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.locators import MainPageLocators
from pages.locators import BasketPageLocators
import pytest

@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page(*MainPageLocators.LOGIN_LINK)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page(*BasketPageLocators.BASKET_BUTTON)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    
@pytest.mark.xfail     
def test_guest_can_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page(*BasketPageLocators.BASKET_BUTTON)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_filled_basket()