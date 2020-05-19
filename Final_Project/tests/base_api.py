import pytest

from api.client import ApiClient
from DB.connector import DBUser


class UserNotFoundException(Exception):
    pass


class BaseCase:
    data = None

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request):
        self.api_client: ApiClient = request.getfixturevalue('api_client')
        self.db: DBUser = request.getfixturevalue('db_user')
