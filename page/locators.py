from selenium.webdriver.common.by import By


class MainPageLocators():
    pass


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class LoginPageLocators():
    login = (By.ID, "login_form")
    register = (By.ID, "register_form")


class ProductPageLocators():
    ADD_BOOK = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")


class BasketLocators():
    ADD_BOOK = (By.XPATH, " //div[@id='messages']//div[1]//div[1]")
    NAME_BOOK_IN_MESSAGE = (By.CSS_SELECTOR, "div:nth-of-type(1) > .alertinner > strong")
    NAME_BOOK_IN_BASKET = (By.TAG_NAME, "h1")
    MESS_COAST_BASKET = (By.XPATH, "//p[contains(text(),'Your basket total is now')]")
    COAST_BASKET = (By.CSS_SELECTOR, ".alert.alert-info.alert-noicon.alert-safe.fade strong")
    COAT_BOOK = (By.CSS_SELECTOR, "[class='col-sm-6 product_main'] .price_color")
