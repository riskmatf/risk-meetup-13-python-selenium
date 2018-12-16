from pages.base import BasePage
from selenium.webdriver.common.by import By


class RepositoryPage(BasePage):

    starLocator = (By.PARTIAL_LINK_TEXT, 'Star')

    def click_on_star(self):
        self.click_on_element(self.starLocator)



