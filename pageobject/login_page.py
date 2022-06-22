from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    email_input_field = (By.CSS_SELECTOR, "input[id='email']")
    passwd_input_field  = (By.CSS_SELECTOR, "input[id='passwd']")
    sign_in_btn = (By.CSS_SELECTOR, "button[id='SubmitLogin']")


    def get_email_input_field(self):
        return self.driver.find_element(*LoginPage.email_input_field)

    def get_passwd_input_field(self):
        return self.driver.find_element(*LoginPage.passwd_input_field)

    def get_sign_in_btn(self):
        return self.driver.find_element(*LoginPage.sign_in_btn)
