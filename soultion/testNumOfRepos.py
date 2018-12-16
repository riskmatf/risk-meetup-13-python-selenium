from pages.login import LoginPage
from pages.homepage import HomePage
from pages.search_results import SearchResultsPage
from pages.user import UserPage
from selenium import webdriver

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
import time

driver = webdriver.Remote('http://127.0.0.1:4444/wd/hub', DesiredCapabilities.CHROME)
homePage = HomePage(driver)
loginPage = LoginPage(driver)
searchPage = SearchResultsPage(driver)
userPage = UserPage(driver)

try:
    homePage.navigate_to_homepage()
    homePage.navigate_to_login()
    loginPage.login_into_page()
    homePage.search_for_user("riskmatf")
    searchPage.navigate_to_user_results()
    searchPage.select_first_user()
    repoBanner = userPage.get_number_of_repos_from_banner()
    realRepo = userPage.get_real_number_of_repos()

    assert realRepo == repoBanner, "Repo and real not the same"

except Exception as e:
    raise e

finally:
    driver.close()
