from pages.base import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage(BasePage):

    userLine = (By.XPATH, "//nav[contains(@class,'menu')]//a[contains(text(),'Users')]")
    userResults = (By.XPATH, "//*[@id='user_search_results']//a")

    def navigate_to_user_results(self):
        self.click_on_element(self.userLine)

    def select_first_user(self):
        print("Selecting first user")
        self.wait_for_element_to_be_clickable(self.userResults)
        results = self.driver.find_elements(*self.userResults)
        results[0].click()
