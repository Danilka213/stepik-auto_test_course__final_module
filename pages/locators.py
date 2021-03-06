from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    
class LoginPageLocators():
    FORM_LOGIN = (By.CSS_SELECTOR, "#login_form")
    FORM_REGISTRATION = (By.CSS_SELECTOR, "#register_form")
    EMAIL_INPUT = (By.CSS_SELECTOR, "#register_form #id_registration-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#register_form #id_registration-password1")
    PASSWORD_CONFIRM_INPUT = (By.CSS_SELECTOR, "#register_form #id_registration-password2")
    BUTTON_REGISTRATION = (By.CSS_SELECTOR, "[name='registration_submit']")
    
class ProductPageLocators():
    BACKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_PRODUCT_IN_BACKET = (By.CSS_SELECTOR, ".alertinner strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRICE_PRODUCT_IN_BACKET = (By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade .alertinner p strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    
class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    MESSAGE_BASKET_IT_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
    CONTAINER_PRODUCTS_IN_THE_BASKET = (By.CSS_SELECTOR, ".basket-items")
    BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a.btn.btn-default")
    
    