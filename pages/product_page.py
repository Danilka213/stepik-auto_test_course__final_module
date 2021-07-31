from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import TimeoutException

class ProductPage(BasePage):
    def should_be_login_page(self):
        self.should_be_front_add_product_in_backet()
        self.add_product_in_backet()
        self.should_be_visible_after_add_product_in_backet()

    def should_be_front_add_product_in_backet(self):
        self.should_be_product_promo_url()
        self.should_not_be_success_message(*ProductPageLocators.MESSAGE_ADD_PRODUCT_IN_BACKET)
        self.should_be_presented_button_backet(*ProductPageLocators.BACKET_BUTTON)
        
    def add_product_in_backet(self):
        self.go_to_product_page(*ProductPageLocators.BACKET_BUTTON)

    def should_be_visible_after_add_product_in_backet(self):
        self.solve_quiz_and_get_code()
        self.should_be_visible_message_add_product_in_backet(*ProductPageLocators.NAME_PRODUCT, *ProductPageLocators.MESSAGE_ADD_PRODUCT_IN_BACKET)
        self.should_be_visible_price_product_in_backet(*ProductPageLocators.PRICE_PRODUCT, *ProductPageLocators.PRICE_PRODUCT_IN_BACKET)
        
    def should_be_product_promo_url(self):
        assert "promo=" in self.browser.current_url, "In url not substrings 'promo='"
        
    def should_be_presented_button_backet(self, how, what):
        assert self.is_element_present(how, what), "backet button is not presented"
        
    def go_to_product_page(self, how,  what):
        link = self.browser.find_element(how,  what)
        self.browser.execute_script("return arguments[0].scrollIntoView(true);", link)
        link.click()

    def should_be_visible_message_add_product_in_backet(self, how_wait, what_wait, how_reality, what_reality):
        print ("Name product: ",self.search_element(how_wait, what_wait).text)
        print ("Message add product in backet: ", self.search_element(how_reality, what_reality ).text)
        assert self.search_element(how_wait, what_wait).text == self.search_element(how_reality, what_reality).text, "product is not add in backet"
        
    def should_be_visible_price_product_in_backet(self, how_wait, what_wait, how_reality, what_reality):
        print ("Price product: ",self.search_element(how_wait, what_wait).text)
        print ("Price in backet: ", self.search_element(how_reality, what_reality).text)
        assert self.search_element(how_wait, what_wait).text == self.search_element(how_reality, what_reality).text, "price product is not in backet" 
        
    def should_not_be_success_message(self, how, what):
        assert self.is_not_element_present(how, what ), \
        "Success message is presented, but should not be"
        
        
