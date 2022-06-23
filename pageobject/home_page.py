from selenium.webdriver.common.by import By

from pageobject.basepage import BasePage
from pageobject.login_page import LoginPage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    sign_in_btn = (By.CSS_SELECTOR, "a[class='login']")
    sign_out_btn = (By.CSS_SELECTOR, "a[class='logout']")

    def get_sign_in_btn(self):
        self.driver.find_element(*HomePage.sign_in_btn).click()
        loginpage = LoginPage(self.driver)
        return loginpage

    def get_signout_btn(self):
        return self.driver.find_element(*HomePage.sign_out_btn)