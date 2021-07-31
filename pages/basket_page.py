from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import TimeoutException

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        self.should_be_is_not_visible_container_products_in_the_basket()
        self.should_be_visible_message_that_basket_is_empty()
        
    def should_be_filled_basket(self):
        self.should_be_visible_container_products_in_the_basket()
        self.should_be_is_not_visible_message_that_basket_is_empty()
        
    def should_be_is_not_visible_container_products_in_the_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTAINER_PRODUCTS_IN_THE_BASKET) is not True, "Container products in the basket visible"
        
    def should_be_visible_container_products_in_the_basket(self):
        assert self.is_element_present(*BasketPageLocators.CONTAINER_PRODUCTS_IN_THE_BASKET), "Container products in the basket not visible"
        
    def should_be_visible_message_that_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IT_EMPTY), "is not message that basket is empty"
        
    #def should_be_is_not_visible_message_that_basket_is_empty(self):
        #assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_IT_EMPTY) is not True, "Visible message that basket is empty"
       
       