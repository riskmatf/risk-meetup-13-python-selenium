from pages.base import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class UserPage(BasePage):

    counterBanner = (By.CSS_SELECTOR, "a.pagehead-tabs-item.selected span.Counter")
    selectorRepos = (By.CSS_SELECTOR, 'div.org-repos.repo-list li h3 a')
    repository = '//a[contains(text(), "{0}")]'

    # get num x2 + goto repo
