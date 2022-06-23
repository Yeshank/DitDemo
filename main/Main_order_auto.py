import inspect

import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobject.cart_page import CartPage
from pageobject.home_page import HomePage
from pageobject.product_page import ProductPage
from pageobject.shop_page import ShopPage
import logging

# @pytest.fixture()
# def driver_instance(browser_invocation):
#     yield browser_invocation
class Test_OrderAuto:


    def test_login(self, login_info, browser_invocation):
        # Creating object of Homepage class to access the elements of Homepage
        homepage = HomePage(browser_invocation)

        # Clicking on the signin button and getting the object of LoginPage class
        loginpage = homepage.get_sign_in_btn()

        # Entering the USERID
        loginpage.get_email_input_field().send_keys(login_info['user_id'])

        # Entering the Password
        loginpage.get_passwd_input_field().send_keys(login_info['passwd'])

        # clicking on the signin Button
        loginpage.get_sign_in_btn().click()

        # Logging the message
        homepage.message_logging('Login Successful')

    def test_shop(self, product_info, browser_invocation):
        # Creating the object of Shop page class to access the elements of shop page class
        shoppage = ShopPage(browser_invocation)

        # Entering the product name which we want to search
        shoppage.get_search_input_field().send_keys(product_info['product_name'])

        # Clicking on the submit search button
        shoppage.get_search_btn().click()

        # clicking on the product to extract it's information
        shoppage.get_product().click()
        # Logging the message
        shoppage.message_logging('Product search Successfull')

    def test_product(self, browser_invocation):
        # Creating the object of ProductPage class to access the elements of product
        product_page = ProductPage(browser_invocation)

        # Getting the product name
        product_page.message_logging(product_page.get_product_name().text)

        # Getting the Condition of the product
        product_page.message_logging(product_page.get_product_condition().text)

        # Getting the product description
        product_page.message_logging(product_page.get_product_description().text)

        # Getting the product price
        product_page.message_logging(product_page.get_product_price().text)

        # Adding the product to the cart
        product_page.get_add_to_cart_btn().click()

        # Logging the message
        product_page.message_logging('Product added to cart')

    def test_cart(self, browser_invocation):
        # Creating the object of CartPage class to access the success text
        cartpage = CartPage(browser_invocation)

        # Waiting until the text is displayed
        cartpage.wait_presence(CartPage.success_text)

        # Getting the Success text which is displayed on the cart page
        cartpage.message_logging(cartpage.get_success_text())

        # waiting until the continue shopping button to be clickable
        cartpage.wait_clickable(cartpage.continue_shopping_btn)

        # CLicking on the continue shopping button
        cartpage.get_continue_shopping_btn().click()

    def test_signout(self, browser_invocation):
        # Creating the object of HomePage class to access the signout button
        homepage = HomePage(browser_invocation)

        # Clicking on sign-out button
        homepage.get_signout_btn().click()

        homepage.message_logging('Sign Out Successfull')