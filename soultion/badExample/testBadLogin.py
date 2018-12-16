from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
import time


try:
    driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    wait = WebDriverWait(driver, 10)
    driver.get("https://github.com")

    driver.find_element_by_partial_link_text("Sign in").click()
    driver.find_element_by_id("login_field").send_keys("riskmatfTest@gmail.com")
    driver.find_element_by_id("password").send_keys("riskmatf1234")
    driver.find_element_by_name("commit").click()

    driver.find_element_by_name("q").send_keys("riskmatf")
    driver.find_element_by_name("q").send_keys(Keys.RETURN)

    usersLine = (By.XPATH, "//nav[contains(@class,'menu')]//a[contains(text(),'Users')]")
    wait.until(EC.element_to_be_clickable(usersLine))
    driver.find_element(*usersLine).click()

    listUsers = (By.XPATH, "//*[@id='user_search_results']//a")
    wait.until(EC.element_to_be_clickable(listUsers))
    users = driver.find_elements(*listUsers)
    users[0].click()

    repositories = (By.CSS_SELECTOR, "a.pagehead-tabs-item.selected")
    wait.until(EC.element_to_be_clickable(repositories))
    driver.find_element(*repositories).click()

    counter = (By.CSS_SELECTOR, "a.pagehead-tabs-item.selected span.Counter")
    wait.until(EC.element_to_be_clickable(counter))
    numberOfRepos = int(driver.find_element(*counter).text)

    selectorRepos = (By.CSS_SELECTOR, 'div.org-repos.repo-list li h3 a')
    repositories = driver.find_elements(*selectorRepos)
    realNumOfRepos = len(repositories)

    assert realNumOfRepos == numberOfRepos, 'Number of elements are not the same'

except WebDriverException as e:
    raise e

finally:
    driver.close()
