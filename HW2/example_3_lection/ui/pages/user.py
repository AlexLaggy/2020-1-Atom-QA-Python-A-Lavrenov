import os

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators import basic_locators
import allure

RETRY_COUNT = 3


class UserPage:
    def __init__(self, driver, login, password):
        self.driver = driver
        self.email = login
        self.password = password

    def find(self, locator, timeout=None) -> WebElement:
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def alert(self, msg):
        script = "alert('{}')".format(msg)
        self.driver.execute_script(script)

    @allure.step('Clicking on {locator}...')
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

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def count_elements(self, locator, count, timeout=1):
        self.wait(timeout).until(lambda browser: len(browser.find_elements(*locator)) == count)

    def login(self) -> WebElement:
        self.find(basic_locators.LOGIN_BUTTON_MAIN_PAGE).click()
        login_email = self.find(basic_locators.EMAIL_LOCATOR)
        login_email.clear()
        login_email.send_keys(self.email)
        login_password = self.find(basic_locators.PASSWORD_LOCATOR)
        login_password.clear()
        login_password.send_keys(self.password)
        return self.find(basic_locators.LOGIN_BUTTON_LOGIN_FORM).click()
