from pages.base import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    # Class implements actions on homepage (login, search)

    search_panel = (By.NAME, "q")
    login_button = (By.PARTIAL_LINK_TEXT, "Sign in")

    # login navigate , search for user

