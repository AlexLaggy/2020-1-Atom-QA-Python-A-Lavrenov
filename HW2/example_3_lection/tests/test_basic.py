import pytest

from selenium.webdriver.support import expected_conditions as EC
from tests.base import BaseCase


class Test(BaseCase):

    @pytest.mark.UI
    def test_login(self):
        self.user_page.login()
        self.user_page.find(self.user_page.locators.CHECK_LOGIN_COMPANY, timeout=3)
        assert "Кампании" in self.driver.page_source

    @pytest.mark.UI
    def test_login_error(self):
        self.user_page.login(False)
        assert "Invalid login or password" in self.driver.page_source

    @pytest.mark.UI
    @pytest.mark.parametrize('url,header,text,file_path, company_name',
                             [('mail.ru', 'Test', 'Test', 'Test2.jpg', 'AlexTest')])
    def test_create_advertising_company(self, url, header, text, file_path, company_name):
        self.user_page.login()
        self.company_page.wait(3)
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

        self.company_page.upload_image(file_path, self.company_page.locators.COMPANY_UPLOAD_JPG_PATH,
                                       self.company_page.locators.COMPANY_UPLOAD_JPG_SEND)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_UPLOAD_JPG)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_UPLOAD_JPG_KOSTIL)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_TIZER)
        self.company_page.click(self.company_page.locators.COMPANY_CONFIRM_CREATE)
        self.company_page.find(self.company_page.locators.COMPANY_STATES_DELETED, timeout=3)
        assert company_name in self.driver.page_source

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
        self.segment_page.click(self.segment_page.locators.SEGMENT_FIND_BY_NAME)
        assert segment_name in self.driver.page_source

        # Delete segment
        self.segment_page.click(self.segment_page.locators.SEGMENT_REMOVE)
        self.segment_page.click(self.segment_page.locators.SEGMENT_REMOVE_CONFIRM)

        # Check deleted
        self.segment_page.search(segment_name, self.segment_page.locators.SEGMENT_FIND_CREATED_NAME)
        self.segment_page.find(self.segment_page.locators.SEGMENT_WAIT)

        print(self.driver.page_source)
        assert "Ничего не найдено ..." in self.driver.page_source
