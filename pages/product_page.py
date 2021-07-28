from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_login_page(self):
        self.should_be_product_promo_url()
        self.should_be_presented_button_backet()
        self.go_to_product_page(*ProductPageLocators.BACKET_BUTTON)
        self.solve_quiz_and_get_code()
        self.should_be_visible_message_add_product_in_backet()
        self.should_be_visible_price_product_in_backet()

    def should_be_product_promo_url(self):
        assert "promo=newYea" in self.browser.current_url, "In url not substrings 'promo=newYea'"
        
    def should_be_presented_button_backet(self):
        assert self.is_element_present(*ProductPageLocators.BACKET_BUTTON), "backet button is not presented"
        
    def go_to_product_page(self, how,  what):
        link = self.browser.find_element(how,  what)
        link.click()

    def should_be_visible_message_add_product_in_backet(self):
        name_product_in_backet = self.search_element(*ProductPageLocators.MESSAGE_ADD_PRODUCT_IN_BACKET)
        assert "The shellcoder's handbook" in name_product_in_backet.text, "product is not add in backet"
        
    def should_be_visible_price_product_in_backet(self):
        price_product_in_backet = self.search_element(*ProductPageLocators.PRICE_PRODUCT_IN_BACKET)
        assert "9,99" in price_product_in_backet.text, "price product is not in backet" 
        
