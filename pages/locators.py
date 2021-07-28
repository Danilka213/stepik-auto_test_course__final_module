from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
    
    
class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    
    
class ProductPageLocators():
    BACKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_PRODUCT_IN_BACKET = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_PRODUCT_IN_BACKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade .alertinner p strong")
    