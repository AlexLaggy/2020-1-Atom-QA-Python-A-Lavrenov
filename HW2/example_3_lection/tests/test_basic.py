import pytest
from selenium.webdriver.common.by import By

import time

from tests.base import BaseCase


class Test(BaseCase):

    # @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_login(self):
        self.user_page.login()
        time.sleep(3)
        assert "Кампании" in self.driver.page_source

    # @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    def test_login_error(self):
        self.user_page.login(False)
        time.sleep(3)
        assert "Invalid login or password" in self.driver.page_source

    # @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    @pytest.mark.parametrize('url,header,text,file_path, company_name',
                             [('mail.ru', 'Test', 'Test', 'Test2.jpg', 'AlexTest')])
    def test_create_advertising_company(self, url, header, text, file_path, company_name):
        self.user_page.login()
        time.sleep(3)
        self.company_page.click(self.company_page.locators.COMPANY_STATES)
        self.company_page.click(self.company_page.locators.COMPANY_STATES_DELETED)
        self.company_page.click(self.company_page.locators.COMPANY_CREATE)
        self.company_page.click(self.company_page.locators.COMPANY_TARGET)
        self.company_page.search(url, self.company_page.locators.COMPANY_INPUT_URL)
        self.company_page.click(self.company_page.locators.COMPANY_CLEAR_NAME)
        self.company_page.search(company_name, self.company_page.locators.COMPANY_INPUT_NAME)
        self.company_page.click(self.company_page.locators.COMPANY_TIZER)
        self.company_page.search(header, self.company_page.locators.COMPANY_HEADER)
        self.company_page.search(text, self.company_page.locators.COMPANY_TEXT)
        # self.click(basic_locators.COMPANY_DELETE_EXISTS_IMG)
        # self.click(basic_locators.COMPANY_CONFIRM_DELETE_EXISTS_IMG)
        self.company_page.upload_image(file_path, self.company_page.locators.COMPANY_UPLOAD_JPG_PATH,
                                       self.company_page.locators.COMPANY_UPLOAD_JPG_SEND)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_UPLOAD_JPG)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_UPLOAD_JPG_KOSTIL)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_TIZER)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_CREATE)
        time.sleep(5)
        assert company_name in self.driver.page_source

    # @pytest.mark.skip(reason='TEMP')
    @pytest.mark.UI
    @pytest.mark.parametrize('segment_name', ['AlexTest'])
    def test_create_segment(self, segment_name):
        self.user_page.login()
        self.segment_page.click(self.segment_page.locators.SEGMENT_MAIN)
        self.segment_page.click(self.segment_page.locators.SEGMENT_CREATE)
        self.segment_page.click(self.segment_page.locators.SEGMENT_CREATE_AUDIT_SEGMENT)
        self.segment_page.click(self.segment_page.locators.SEGMENT_CREATE_AUDIT_USER_LIST)
        self.segment_page.click(self.segment_page.locators.SEGMENT_CREATE_AUDIT_ADD_CHOOSE)
        self.segment_page.click(self.segment_page.locators.SEGMENT_CREATE_AUDIT_ADD)
        self.segment_page.search(segment_name, self.segment_page.locators.SEGMENT_CREATE_AUDIT_NAME)
        self.segment_page.click(self.segment_page.locators.SEGMENT_CREATE_BUTTON)

        # Check created
        self.segment_page.search(segment_name, self.segment_page.locators.SEGMENT_FIND_CREATED_NAME)
        self.segment_page.click((By.XPATH, f'//span[@title="{segment_name}"]'))
        assert segment_name in self.driver.page_source

        # Delete segment
        self.segment_page.click(self.segment_page.locators.SEGMENT_REMOVE)
        self.segment_page.click(self.segment_page.locators.SEGMENT_REMOVE_CONFIRM)
        time.sleep(3)

        assert segment_name not in self.driver.page_source
