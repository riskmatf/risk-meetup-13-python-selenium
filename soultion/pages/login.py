from selenium.webdriver.common.by import By
from base import BasePage
import time


class LoginPage(BasePage):

    loginField = (By.ID, "login_field")
    passwordField = (By.ID, "password")
    submitLogin = (By.NAME, "commit")

    # login , validate login
