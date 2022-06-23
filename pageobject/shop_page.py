from selenium.webdriver.common.by import By

from pageobject.basepage import BasePage


class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_input_field = (By.CSS_SELECTOR, "input[id='search_query_top']")
    submit_search_btn = (By.CSS_SELECTOR, "button[name='submit_search']")
    product = (By.CSS_SELECTOR, "div[class='right-block'] h5 a[class='product-name']")

    def get_search_input_field(self):
        return self.driver.find_element(*ShopPage.search_input_field)

    def get_search_btn(self):
        return self.driver.find_element(*ShopPage.submit_search_btn)

    def get_product(self):
        return self.driver.find_element(*ShopPage.product)