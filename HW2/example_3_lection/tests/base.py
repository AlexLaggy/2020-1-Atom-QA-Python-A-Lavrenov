import pytest
from ui.pages.base import BasePage
from ui.pages.company import CompanyPage
from ui.pages.segment import SegmentPage
from ui.pages.user import UserPage


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, driver, request):
        self.config = config
        self.driver = driver
        self.user_page: UserPage = request.getfixturevalue('user_page')
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.company_page: CompanyPage = request.getfixturevalue('company_page')
        self.segment_page: SegmentPage = request.getfixturevalue('segment_page')
        # self.user_page.login()
