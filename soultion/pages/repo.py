from pages.base import BasePage
from selenium.webdriver.common.by import By


class RepositoryPage(BasePage):

    starLocator = (By.PARTIAL_LINK_TEXT, 'Star')

    # click star



