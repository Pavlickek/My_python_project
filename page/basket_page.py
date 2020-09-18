from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def basket_is_empty(self):
        assert self.is_not_element_present(*BasketLocators.STRING_IF_BASKET_HAS_GOODS), ("Basket is not empty")

    def string_about_basket_is_empty(self):
        assert self.is_element_present(*BasketLocators.STRING_ABOUT_BASKET_IS_EMPTY), ("Basket dodnt has element")
