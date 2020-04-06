import pytest
from ui.fixtures import *
from dataclasses import dataclass

import pytest
from api.client import ApiClient


# @dataclass
# class Settings:
#     URL: str = None
#
#
# @pytest.fixture(scope='session')
# def conf() -> Settings:
#     settings = Settings(URL='https://target.my.com')
#
#     return settings
#
#
# @pytest.fixture(scope='function')
# def api_client(conf):
#     return ApiClient(conf.URL)


class UsupportedBrowserException(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--login', default='LagAlexTest@ya.ru')
    parser.addoption('--password', default='LagAlex')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    login = request.config.getoption('--login')
    password = request.config.getoption('--password')

    return {'browser': browser, 'version': version, 'url': url,
            'download_dir': '/tmp', 'login': login, 'password': password}
