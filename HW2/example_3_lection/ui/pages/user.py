from .base import BasePage

from selenium.webdriver.remote.webelement import WebElement
from ui.locators.basic_locators import BaseLocators
import allure


class UserPage(BasePage):
    locators = BaseLocators

    def __init__(self, driver, login, password):
        super().__init__(driver)
        self.email = login
        self.password = password

    def login(self, make_error=True) -> WebElement:
        self.click(self.locators.LOGIN_BUTTON_MAIN_PAGE)
        self.search(self.email, self.locators.EMAIL_LOCATOR)
        self.search(self.password if make_error else 'error', self.locators.PASSWORD_LOCATOR)
        return self.click(self.locators.LOGIN_BUTTON_LOGIN_FORM)
