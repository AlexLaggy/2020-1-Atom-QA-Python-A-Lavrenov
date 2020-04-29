import pytest
from ui.fixtures import *
from api.fixtures import *


class UsupportedBrowserException(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--url', default='https://target.my.com/')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--login', default='LagAlexTest@ya.ru')
    parser.addoption('--password', default='LagAlex')
    parser.addoption('--selenoid', default=None)


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    login = request.config.getoption('--login')
    password = request.config.getoption('--password')
    selenoid = request.config.getoption('--selenoid')

    return {'browser': browser, 'version': version, 'url': url,
            'download_dir': '/tmp', 'login': login, 'password': password, 'selenoid': selenoid}
