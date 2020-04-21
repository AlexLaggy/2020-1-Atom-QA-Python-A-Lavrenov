import os

from .base import BasePage
from ui.locators.basic_locators import CompanyLocators


class CompanyPage(BasePage):
    locators = CompanyLocators()

    def upload_image(self, file_path, file_locator, button_locator):
        current_file_dir = os.path.dirname(__file__)
        abs_file_path = os.path.abspath(os.path.join(current_file_dir, os.path.pardir, os.path.pardir, file_path))
        search_field = self.find(file_locator)
        search_field.send_keys(abs_file_path)
        self.find(button_locator).click()
