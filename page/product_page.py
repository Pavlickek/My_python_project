from .base_page import BasePage
from .locators import ProductPageLocators, BasketLocators




class ProductPage(BasePage):


      def add_books_in_basket(self):

          button = self.browser.find_element(*ProductPageLocators.ADD_BOOK)
          button.click()
          self.solve_quiz_and_get_code()


      def add_books_in_basket_nigative(self):
          button = self.browser.find_element(*ProductPageLocators.ADD_BOOK)
          button.click()


      def should_not_be_success_message(self):
          assert self.is_not_element_present(*BasketLocators.ADD_BOOK),(
              "Success message is presented, but should not be")


      def success_message_is_disappeared(self):
          assert self.is_disappeared(*BasketLocators.ADD_BOOK), (
              "Success message didnt disappear")


      def should_be_in_basket(self):
          self.message_book_add_in_basket()
          self.massage_of_book_should_be_equal_picked_book()
          self.massage_of_coast_of_basket()
          self.coast_of_basket_equal_coast_of_book()

      def message_book_add_in_basket(self):
          assert self.is_element_present(*BasketLocators.ADD_BOOK), ("Message about adding is not presented")
          assert True


      def massage_of_book_should_be_equal_picked_book(self):
          assert self.is_element_present(*BasketLocators.NAME_BOOK_IN_MESSAGE), ("Name of book in message didnt found")
          assert self.is_element_present(*BasketLocators.NAME_BOOK_IN_BASKET), ("Name of book in basket didnt found")
          NAME_BOOK_IN_MESSAGE = self.browser.find_element(*BasketLocators.NAME_BOOK_IN_MESSAGE).text
          NAME_BOOK_IN_BASKET = self.browser.find_element(*BasketLocators.NAME_BOOK_IN_BASKET).text
          assert NAME_BOOK_IN_MESSAGE == NAME_BOOK_IN_BASKET, ("Name of book in message not equal name of book in basket")
          assert True


      def massage_of_coast_of_basket(self):
          assert self.is_element_present(*BasketLocators.MESS_COAST_BASKET), ("Message about coast of basket is not presented")
          assert True



      def coast_of_basket_equal_coast_of_book(self):
           assert self.is_element_present(*BasketLocators.COAST_BASKET), ("Coast of book in basket didnt found")
           assert self.is_element_present(*BasketLocators.COAT_BOOK), ("Coast of book  didnt found")
           COAST_OF_BASKET = self.browser.find_element(*BasketLocators.COAST_BASKET).text
           COAST_OF_BOOK = self.browser.find_element(*BasketLocators.COAT_BOOK).text
           assert COAST_OF_BASKET == COAST_OF_BOOK, ("Coast of book  not equal coast of book in basket")
           assert True


