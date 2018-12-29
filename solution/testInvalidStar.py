from pages.login import LoginPage
from pages.homepage import HomePage
from pages.search_results import SearchResultsPage
from pages.user import UserPage
from pages.repo import RepositoryPage
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
import time

driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', DesiredCapabilities.CHROME)
homePage = HomePage(driver)
loginPage = LoginPage(driver)
searchPage = SearchResultsPage(driver)
userPage = UserPage(driver)
repoPage = RepositoryPage(driver)

try:
    homePage.navigate_to_homepage()
    homePage.search_for_user("riskmatf")
    searchPage.navigate_to_user_results()
    searchPage.select_first_user()
    userPage.go_to_repository("risk-media")
    repoPage.click_on_star()

    assert loginPage.validate_login_page(), "Login page not displayed"

except Exception as e:
    raise e

finally:
    driver.close()
