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
    assert True

except Exception as e:
    raise e

finally:
    driver.close()
