from selenium.webdriver.common.by import By

from pageobject.basepage import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    product_name = (By.CSS_SELECTOR, "h1[itemprop='name']")
    product_condition = (By.CSS_SELECTOR, "p[id='product_condition'] span")
    product_description = (By.CSS_SELECTOR, "div[id='short_description_content'] p")
    product_price = (By.CSS_SELECTOR, "span[id='our_price_display']")
    add_to_cart_btn = (By.CSS_SELECTOR, "div[class='box-cart-bottom'] button")

    def get_product_name(self):
        return self.driver.find_element(*ProductPage.product_name)

    def get_product_condition(self):
        return self.driver.find_element(*ProductPage.product_condition)

    def get_product_description(self):
        return self.driver.find_element(*ProductPage.product_description)

    def get_product_price(self):
        return self.driver.find_element(*ProductPage.product_price)

    def get_add_to_cart_btn(self):
        return self.driver.find_element(*ProductPage.add_to_cart_btn)