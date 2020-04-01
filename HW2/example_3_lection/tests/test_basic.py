import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

from tests.base import BaseCase
from ui.locators import basic_locators


class Test(BaseCase):

    @pytest.mark.skip(reason='TEMP')
    def test_basic(self):
        assert 'Python' in self.driver.title

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.parametrize('query', ['pycon', 'python'])
    def test_search(self, query):
        self.search(query)
        assert "No results found." not in self.driver.page_source

    @pytest.mark.skip(reason='TEMP')
    def test_login(self): # TODO: Done with fixture
        self.user_page.login()
        time.sleep(5)
        print(self.driver.page_source)
        assert "С чего начать?" in self.driver.page_source

    @pytest.mark.skip(reason='TEMP')
    @pytest.mark.parametrize('url,header,text,file_path, company_name',
                             [('mail.ru', 'Test', 'Test', 'Test2.jpg', 'AlexTest')])
    def test_create_advertising_company(self, url, header, text, file_path, company_name):
        self.user_page.login()
        time.sleep(3)
        self.click(basic_locators.COMPANY_STATES)
        self.click(basic_locators.COMPANY_STATES_DELETED)
        self.click(basic_locators.COMPANY_CREATE)
        self.click(basic_locators.COMPANY_TARGET)
        self.search_by_locator(url, basic_locators.COMPANY_INPUT_URL)
        self.click(basic_locators.COMPANY_CLEAR_NAME)
        self.search_by_locator(company_name, basic_locators.COMPANY_INPUT_NAME)
        self.click(basic_locators.COMPANY_TIZER)
        self.search_by_locator(header, basic_locators.COMPANY_HEADER)
        self.search_by_locator(text, basic_locators.COMPANY_TEXT)
        # self.click(basic_locators.COMPANY_DELETE_EXISTS_IMG)
        # self.click(basic_locators.COMPANY_CONFIRM_DELETE_EXISTS_IMG)
        self.upload_image(file_path, basic_locators.COMPANY_UPLOAD_JPG_PATH, basic_locators.COMPANY_UPLOAD_JPG_SEND)
        self.click(basic_locators.COMPANY_CONFIRM_UPLOAD_JPG)
        self.click(basic_locators.COMPANY_CONFIRM_UPLOAD_JPG_KOSTIL)
        self.click(basic_locators.COMPANY_CONFIRM_TIZER)
        self.click(basic_locators.COMPANY_CONFIRM_CREATE)
        time.sleep(5)
        assert company_name in self.driver.page_source

    # @pytest.mark.skip(reason='TEMP')
    @pytest.mark.parametrize('segment_name', ['AlexTest'])
    def test_create_segment(self, segment_name):
        # self.user_page.login()
        # time.sleep(3)
        self.click(basic_locators.SEGMENT_MAIN)
        time.sleep(3)

        # self.click(basic_locators.SEGMENT_USER_LIST_PAGE)
        # time.sleep(3)
        # self.click(basic_locators.SEGMENT_MAIN)
        # time.sleep(3)
        # self.click(basic_locators.SEGMENT_MAIN)
        # time.sleep(3)
        self.click(basic_locators.SEGMENT_CREATE)
        time.sleep(3)
        self.click(basic_locators.SEGMENT_CREATE_AUDIT_SEGMENT)
        time.sleep(3)
        self.click(basic_locators.SEGMENT_CREATE_AUDIT_USER_LIST)
        time.sleep(3)
        self.click(basic_locators.SEGMENT_CREATE_AUDIT_ADD_CHOOSE)
        time.sleep(3)
        self.click(basic_locators.SEGMENT_CREATE_AUDIT_ADD)
        time.sleep(3)
        self.search_by_locator(segment_name, basic_locators.SEGMENT_CREATE_AUDIT_NAME)
        time.sleep(3)
        self.click(basic_locators.SEGMENT_CREATE_BUTTON)
        time.sleep(3)

        # Check created
        self.search_by_locator(segment_name, basic_locators.SEGMENT_FIND_CREATED_NAME)
        # search = self.find(basic_locators.SEGMENT_FIND_CREATED_NAME)
        # search.clear()
        # search.send_keys(segment_name)
        time.sleep(3)
        self.click((By.XPATH, f'//span[@title="{segment_name}"]'))
        time.sleep(5)
        assert segment_name in self.driver.page_source

        # Delete segment
        self.click(basic_locators.SEGMENT_REMOVE)
        time.sleep(3)
        self.click(basic_locators.SEGMENT_REMOVE_CONFIRM)
        time.sleep(3)

        assert segment_name not in self.driver.page_source


    # @pytest.mark.skip(reason='TEMP')
    # @pytest.mark.parametrize('email,password', [('LagAlexTest@ya.ru', 'LagAlex')])
    # def test_login_good(self, email, password):
    #     self.login_ui(email, password)
    #     assert "С чего начать?" in self.driver.page_source
    #
    # # @pytest.mark.skip(reason='TEMP')
    # @pytest.mark.parametrize('email,password', [('LagAlexTest@ya.ru', 'Lag')])
    # def test_login_bad(self, email, password):
    #     self.login_ui(email, password)
    #     assert "Invalid login or password" in self.driver.page_source # TODO: worked auth

    @pytest.mark.skip(reason='TEMP')
    def test_search_negative(self):
        self.search('23132173152361253675216735126735132516736712')
        self.find(basic_locators.NO_RESULTS).is_displayed()

    @pytest.mark.skip(reason='TEMP')
    def test_carousel(self):
        self.click(basic_locators.COMPREHENSIONS, timeout=12)

    @pytest.mark.skip(reason='TEMP')
    def test_count(self):
        with pytest.raises(TimeoutException):
            self.count_elements(basic_locators.NO_SUCH_ELEMENT, count=2)

    @pytest.mark.skip(reason='TEMP')
    def test_euro_python(self):
        events = self.find(basic_locators.EVENTS)

        ac = ActionChains(self.driver)
        ac.move_to_element(events).perform()

        self.click(basic_locators.PYTHON_EVENTS)
        self.click(basic_locators.EURO_PYTHON)

        assert 'Dublin' in self.driver.page_source

    @pytest.mark.skip(reason='TEMP')
    def test_page_changed(self):
        self.click(basic_locators.GO_BUTTON)

    @pytest.mark.skip(reason='TEMP')
    def test_relative(self):
        intro = self.find(basic_locators.INTRODUCTION)
        learn_more = intro.find_element(*basic_locators.LEARN_MORE)

        if self.config['url'].startswith('https'):
            expected = self.config['url']
        else:
            expected = self.config['url'].replace('http', 'https')

        assert learn_more.get_attribute('href') == f'{expected}/doc/'

    @pytest.mark.skip(reason='TEMP')
    def test_options(self):
        self.driver.get('https://expired.badssl.com/')
        self.find((By.XPATH, '//*[@id="content"]/h1'))

    @pytest.mark.skip(reason='TEMP')
    def test_download(self):
        self.driver.get('https://www.python.org/downloads/release/python-382/')
        self.click((By.XPATH, '//*[contains(text(), "Windows x86-64 web-based installer")]'))
        self.wait_download('python-3.8.2-amd64-webinstall.exe')
