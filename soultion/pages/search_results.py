from pages.base import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(BasePage):

    userLine = (By.XPATH, "//nav[contains(@class,'menu')]//a[contains(text(),'Users')]")
    userResults = (By.XPATH, "//*[@id='user_search_results']//a")

    # user res, select first user
