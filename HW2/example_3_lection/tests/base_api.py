import pytest

from api.client import ApiClient


class UserNotFoundException(Exception):
    pass


class BaseCase:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, config, request):
        self.api_client: ApiClient = request.getfixturevalue('api_client')
