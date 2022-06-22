import pytest

from utilities.baseclass import BaseClass
from pageobject.cart_page import CartPage
from pageobject.home_page import HomePage
from pageobject.product_page import ProductPage
from pageobject.shop_page import ShopPage


class Test_OrderAuto(BaseClass):

    def test_login(self, login_info):
        # Creating object of Homepage class to access the elements of Homepage
        homepage = HomePage(self.driver)

        # Clicking on the signin button and getting the object of LoginPage class
        loginpage = homepage.get_sign_in_btn()

        # Entering the USERID
        loginpage.get_email_input_field().send_keys(login_info['user_id'])

        # Entering the Password
        loginpage.get_passwd_input_field().send_keys(login_info['passwd'])

        # clicking on the signin Button
        loginpage.get_sign_in_btn().click()

        # Logging the message
        self.message_logging('Login Successful')

    def test_shop(self, product_info):
        # Creating the object of Shop page class to access the elements of shop page class
        shoppage = ShopPage(self.driver)

        # Entering the product name which we want to search
        shoppage.get_search_input_field().send_keys(product_info['product_name'])

        # Clicking on the submit search button
        shoppage.get_search_btn().click()

        # clicking on the product to extract it's information
        shoppage.get_product().click()
        # Logging the message
        self.message_logging('Product search Successfull')

    def test_product(self):
        # Creating the object of ProductPage class to access the elements of product
        product_page = ProductPage(self.driver)

        # Getting the product name
        self.message_logging(product_page.get_product_name().text)

        # Getting the Condition of the product
        self.message_logging(product_page.get_product_condition().text)

        # Getting the product description
        self.message_logging(product_page.get_product_description().text)

        # Getting the product price
        self.message_logging(product_page.get_product_price().text)

        # Adding the product to the cart
        product_page.get_add_to_cart_btn().click()

        # Logging the message
        self.message_logging('Product added to cart')

    def test_cart(self):
        # Creating the object of CartPage class to access the success text
        cartpage = CartPage(self.driver)

        # Waiting until the text is displayed
        self.wait_presence(CartPage.success_text)

        # Getting the Success text which is displayed on the cart page
        self.message_logging(cartpage.get_success_text())

        # waiting until the continue shopping button to be clickable
        self.wait_clickable(cartpage.continue_shopping_btn)

        # CLicking on the continue shopping button
        cartpage.get_continue_shopping_btn().click()

    def test_signout(self):
        # Creating the object of HomePage class to access the signout button
        homepage = HomePage(self.driver)

        # Clicking on sign-out button
        homepage.get_signout_btn().click()

        self.message_logging('Sign Out Successfull')