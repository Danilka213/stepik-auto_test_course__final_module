from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "In url not substrings 'login'"

    def should_be_login_form(self):
        assert  self.is_element_present(*LoginPageLocators.FORM_LOGIN), "Login form is not presented"  

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_REGISTRATION), "Registration form is not presented"  
        
    def register_new_user(self):
        self.enter_value_in_input(*LoginPageLocators.EMAIL_INPUT, self.creation_email())
        self.enter_value_in_input(*LoginPageLocators.PASSWORD_INPUT, self.creation_password())
        self.enter_value_in_input(*LoginPageLocators.PASSWORD_CONFIRM_INPUT, self.search_element(*LoginPageLocators.PASSWORD_INPUT).get_property("value"))
        self.go_to_login_page(*LoginPageLocators.BUTTON_REGISTRATION)  
        
        
    def creation_email(self):
        email = str(time.time()) + "@fakemail.org"
        return email
        
        
    def creation_password(self):
        password = str(time.time())
        return password