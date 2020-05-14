import pytest
from ui.fixtures import *
from api.fixtures import *
from DB.fixtures import *


class UsupportedBrowserException(Exception):
    pass


def pytest_addoption(parser):
    parser.addoption('--url', default='http://app:5555')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--login', default='Akkakiy13')
    parser.addoption('--password', default='qwe')
    parser.addoption('--selenoid', default='selenoid:4444')

    parser.addoption('--db_user', default='test_qa')
    parser.addoption('--db_password', default='qa_test')
    parser.addoption('--db_name', default='test')
    parser.addoption('--db_host', default='mysql_database')
    parser.addoption('--db_port', default='3306')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    login = request.config.getoption('--login')
    password = request.config.getoption('--password')
    selenoid = request.config.getoption('--selenoid')

    db_user = request.config.getoption('--db_user')
    db_password = request.config.getoption('--db_password')
    db_name = request.config.getoption('--db_name')
    db_host = request.config.getoption('--db_host')
    db_port = request.config.getoption('--db_port')

    return {'browser': browser, 'version': version, 'url': url,
            'db_user': db_user, 'db_password': db_password, 'db_name': db_name, 'db_host': db_host, 'db_port': db_port,
            'download_dir': '/tmp', 'login': login, 'password': password, 'selenoid': selenoid}
