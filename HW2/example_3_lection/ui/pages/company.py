import os

from .base import BasePage
from ui.locators.basic_locators import CompanyLocators


class CompanyPage(BasePage):
    locators = CompanyLocators()

    def upload_image(self, file_path, file_locator, button_locator):
        search_field = self.find(file_locator)
        search_field.send_keys(f'{os.getcwd()}/{file_path}')
        self.find(button_locator).click()
