

from selenium.webdriver.common.by import By

from pageobject.basepage import BasePage


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    success_text = (By.XPATH, "//*[@id='layer_cart']/div[1]/div[1]/h2")
    continue_shopping_btn = (By.CSS_SELECTOR, "span[class='continue btn btn-default button exclusive-medium']")

    def get_success_text(self):
        return self.driver.find_element(*CartPage.success_text)

    def get_continue_shopping_btn(self):
        return self.driver.find_element(*CartPage.continue_shopping_btn)