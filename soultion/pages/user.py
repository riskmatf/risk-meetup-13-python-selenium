from pages.base import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UserPage(BasePage):

    counterBanner = (By.CSS_SELECTOR, "a.pagehead-tabs-item.selected span.Counter")
    selectorRepos = (By.CSS_SELECTOR, 'div.org-repos.repo-list li h3 a')
    repository = '//a[contains(text(), "{0}")]'

    def get_number_of_repos_from_banner(self):
        print("Getting num of repositories from baner")
        self.wait_for_element_visibility(self.counterBanner)
        return int(self.driver.find_element(*self.counterBanner).text)

    def get_real_number_of_repos(self):
        print("Getting real num of repositories")
        list_of_repos = self.driver.find_elements(*self.selectorRepos)
        return len(list_of_repos)

    def go_to_repository(self, name):
        print("Going to repository {0}".format(name))
        repo = (By.XPATH, self.repository.format(name))
        self.click_on_element(repo)
