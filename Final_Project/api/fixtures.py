import pytest

from api.client import ApiClient


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='session')
def api_client(config, create_db_user):
    return ApiClient(config['login'], create_db_user['password'], create_db_user['email'], create_db_user['url'])
