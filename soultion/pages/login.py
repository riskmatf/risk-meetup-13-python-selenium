from selenium.webdriver.common.by import By
from base import BasePage
import time


class LoginPage(BasePage):

    loginField = (By.ID, "login_field")
    passwordField = (By.ID, "password")
    submitLogin = (By.NAME, "commit")

    def login_into_page(self, user="riskmatfTest@gmail.com", password="riskmatf1234"):
        print "Logging into user: {0}, {1}".format(user, password)
        self.driver.find_element(*self.loginField).send_keys(user)
        self.driver.find_element(*self.passwordField).send_keys(password)
        self.driver.find_element(*self.submitLogin).click()

    def validate_login_page(self):
        return self.driver.find_element(*self.loginField).is_displayed()
