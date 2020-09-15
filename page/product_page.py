from .base_page import BasePage
from .locators import ProductPageLocators, BasketLocators




class ProductPage(BasePage):


      def add_books_in_basket(self):

          button = self.browser.find_element(*ProductPageLocators.ADD_BOOK)
          button.click()
          self.solve_quiz_and_get_code()


      def should_be_in_basket(self):
          self.message_book_add_in_basket()
          self.massage_of_book_should_be_equal_picked_book()
          self.massage_of_coast_of_basket()
          self.coast_of_basket_equal_coast_of_book()

      def message_book_add_in_basket(self):
          assert self.browser.find_element(*BasketLocators.ADD_BOOK)
          assert True


      def massage_of_book_should_be_equal_picked_book(self):
          NAME_BOOK_IN_MESSAGE = self.browser.find_element(*BasketLocators.NAME_BOOK_IN_MESSAGE).text
          NAME_BOOK_IN_BASKET = self.browser.find_element(*BasketLocators.NAME_BOOK_IN_BASKET).text
          assert NAME_BOOK_IN_MESSAGE == NAME_BOOK_IN_BASKET
          assert True


      def massage_of_coast_of_basket(self):
          assert self.browser.find_element(*BasketLocators.MESS_COAST_BASKET)
          assert True



      def coast_of_basket_equal_coast_of_book(self):
           COAST_OF_BASKET = self.browser.find_element(*BasketLocators.COAST_BASKET).text
           COAST_OF_BOOK = self.browser.find_element(*BasketLocators.COAT_BOOK).text
           assert   COAST_OF_BASKET == COAST_OF_BOOK
           assert True