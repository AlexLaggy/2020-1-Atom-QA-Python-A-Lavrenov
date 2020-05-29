import pytest
from ui.pages.base import BasePage
from ui.pages.registry import RegPage
from ui.pages.main import MainPage
from ui.pages.user import UserPage
from DB.connector import DBUser


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, driver, request):
        self.config = config
        self.driver = driver
        self.user_page: UserPage = request.getfixturevalue('user_page')
        self.base_page: BasePage = request.getfixturevalue('base_page')
        self.reg_page: RegPage = request.getfixturevalue('reg_page')
        self.main_page: MainPage = request.getfixturevalue('main_page')
        self.db: DBUser = request.getfixturevalue('db_user')
