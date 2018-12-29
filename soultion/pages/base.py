from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
import time


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def navigate_to_homepage(self):
        self.driver.get("https://github.com")

    def wait_for_element_visibility(self, locator, waittime=30):
        WebDriverWait(self.driver, waittime).until(EC.visibility_of_element_located(locator))

    def wait_for_element_to_be_not_visibile(self, locator, waittime=30):
        WebDriverWait(self.driver, waittime).until(EC.invisibility_of_element_located(locator))

    def wait_for_element_to_be_clickable(self, locator, waittime=30):
        WebDriverWait(self.driver, waittime).until(EC.element_to_be_clickable(locator))

    def click_on_element(self, locator):
        print("Clicking on element: {0}".format(locator))
        self.wait_for_element_to_be_clickable(locator)
        self.driver.find_element(*locator).click()