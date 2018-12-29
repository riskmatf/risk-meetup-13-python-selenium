from pages.base import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):
    # Class implements actions on homepage (login, search)

    search_panel = (By.NAME, "q")
    login_button = (By.PARTIAL_LINK_TEXT, "Sign in")

    def navigate_to_login(self):
        self.click_on_element(self.login_button)

    def search_for_user(self, query):
        print("Searching for user: {0}".format(query))
        panel = self.driver.find_element(*self.search_panel)
        panel.send_keys(query)
        panel.send_keys(Keys.RETURN)

