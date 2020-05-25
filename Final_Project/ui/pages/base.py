from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators.basic_locators import BaseLocators

RETRY_COUNT = 6


class BasePage:
    locators = BaseLocators()

    def __init__(self, driver):
        self.driver = driver

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def click(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                element = self.wait(timeout).until(EC.element_to_be_clickable(locator))
                element.click()
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise Exception('hello')

    def check(self, locator, timeout=None):
        for i in range(RETRY_COUNT):
            try:
                self.find(locator)
                self.wait(timeout).until(EC.element_to_be_clickable(locator))
                print(self.driver.page_source)
                return

            except StaleElementReferenceException:
                if i < RETRY_COUNT - 1:
                    pass
        raise Exception('hello')

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def search(self, query, locator):
        search_field = self.find(locator)
        search_field.clear()
        search_field.send_keys(query)
