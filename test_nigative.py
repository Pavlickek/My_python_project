from .page.product_page import ProductPage
import pytest

link_for_each_test = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = link_for_each_test
    page = ProductPage(browser, link)
    page.open()
    page.add_books_in_basket_nigative()
    page.should_not_be_success_message()



def test_guest_cant_see_success_message(browser):
    link = link_for_each_test
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()




@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = link_for_each_test
    page = ProductPage(browser, link)
    page.open()
    page.add_books_in_basket_nigative()
    page.success_message_is_disappeared()
