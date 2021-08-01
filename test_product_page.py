from pages.main_page import MainPage
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.locators import ProductPageLocators
from pages.locators import BasePageLocators
from pages.locators import BasketPageLocators
from selenium import webdriver
import pytest
    
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        #self.product = ProductFactory(title = "Best book created by robot")
        #self.link = self.product.link
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        page.should_be_authorized_user()
      
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_page()
        
    def test_user_cant_see_success_message(self, browser): 
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_not_visible_message_add_product_in_backet(*ProductPageLocators.MESSAGE_ADD_PRODUCT_IN_BACKET)
        
@pytest.mark.need_review    
def test_quest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_page()
        
@pytest.mark.parametrize('links', ["0", "1","2","3","4","5","6" , pytest.param("7", marks=pytest.mark.xfail),"8","9" ])
def test_guest_can_add_product_to_basket(browser, links):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_page()
   
@pytest.mark.xfail   
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_backet()
    page.should_be_not_visible_message_add_product_in_backet(*ProductPageLocators.MESSAGE_ADD_PRODUCT_IN_BACKET)
 
def test_quest_cant_see_success_message(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_not_visible_message_add_product_in_backet(*ProductPageLocators.MESSAGE_ADD_PRODUCT_IN_BACKET)

 
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser): 
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_in_backet()
    page.should_be_that_disappears_message_add_product_in_backet(*ProductPageLocators.MESSAGE_ADD_PRODUCT_IN_BACKET)
    
    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page(*BasePageLocators.LOGIN_LINK)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    
@pytest.mark.need_review    
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page(*BasketPageLocators.BASKET_BUTTON)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    
@pytest.mark.xfail    
def test_guest_can_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page(*BasketPageLocators.BASKET_BUTTON)
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_filled_basket()