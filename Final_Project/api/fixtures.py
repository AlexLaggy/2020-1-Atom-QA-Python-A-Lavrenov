import pytest

from api.client import ApiClient


class UsupportedBrowserException(Exception):
    pass


@pytest.fixture(scope='session')
def api_client(config):
    return ApiClient(config['login'], config['password'], config['email'], config['url'])
