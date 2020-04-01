import os

import pytest
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from ui.locators import basic_locators
from ui.pages.user import UserPage

RETRY_COUNT = 3


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request):
        self.driver = driver
        self.config = config
        self.user_page: UserPage = request.getfixturevalue('user_page')
        # self.user_page.login()

    def find(self, locator, timeout=None) -> WebElement:
        print(locator)
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
        raise Exception('fail')

    def scroll_to_element(self, element):
        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def count_elements(self, locator, count, timeout=1):
        self.wait(timeout).until(lambda browser: len(browser.find_elements(*locator)) == count)

    def wait_download(self, file_name, timeout=30):

        def _check_download(_):
            for f in os.listdir(self.config['download_dir']):
                if f.endswith('.crdownload'):
                    return False

            if file_name in os.listdir(self.config['download_dir']):
                return True

            return False

        self.wait(timeout).until(_check_download)

    def search(self, query):
        search_field = self.find(basic_locators.QUERY_LOCATOR)
        search_field.clear()
        search_field.send_keys(query)
        self.find(basic_locators.GO_BUTTON).click()

    def search_by_locator(self, query, locator):
        search_field = self.find(locator)
        search_field.clear()
        search_field.send_keys(query)

    def upload_image(self, file_path, file_locator, button_locator):
        search_field = self.find(file_locator)
        # search_field.clear()
        search_field.send_keys(f'{os.getcwd()}/{file_path}')
        self.find(button_locator).click()

