import pytest
import requests
import allure
import random
from faker import Faker
from ui.fixtures import *
from api.fixtures import *
from DB.fixtures import *


MAX_TEST_COUNT = 50


class UsupportedBrowserException(Exception):
    pass


def pytest_addoption(parser):
    # parser.addoption('--url', default='http://uselessapp:5555')
    parser.addoption('--url', default='http://0.0.0.0:5555')
    parser.addoption('--browser', default='chrome')
    parser.addoption('--browser_ver', default='latest')
    parser.addoption('--login', default='Akkakiy13')
    parser.addoption('--password', default='qwe')
    parser.addoption('--email', default='yas@ya.ru')
    # parser.addoption('--selenoid', default='selenoid:4444')
    # parser.addoption('--selenoid', default='0.0.0.0:4444')
    parser.addoption('--selenoid', default=None)

    parser.addoption('--db_user', default='test_qa')
    parser.addoption('--db_password', default='qa_test')
    parser.addoption('--db_name', default='test')
    # parser.addoption('--db_host', default='mysql_database')
    parser.addoption('--db_host', default='0.0.0.0')
    parser.addoption('--db_port', default='3306')


@pytest.fixture(scope='session')
def config(request):
    url = request.config.getoption('--url')
    browser = request.config.getoption('--browser')
    version = request.config.getoption('--browser_ver')
    login = request.config.getoption('--login')
    password = request.config.getoption('--password')
    email = request.config.getoption('--email')
    selenoid = request.config.getoption('--selenoid')

    db_user = request.config.getoption('--db_user')
    db_password = request.config.getoption('--db_password')
    db_name = request.config.getoption('--db_name')
    db_host = request.config.getoption('--db_host')
    db_port = request.config.getoption('--db_port')

    return {'browser': browser, 'version': version, 'url': url,
            'db_user': db_user, 'db_password': db_password, 'db_name': db_name, 'db_host': db_host, 'db_port': db_port,
            'download_dir': '/tmp', 'login': login, 'password': password, 'selenoid': selenoid, 'email': email}


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def take_screenshot_when_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        allure.attach('\n'.join([a['message'] for a in driver.get_log('browser')]),
                      name='console.log',
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(driver.get_screenshot_as_png(),
                      name=request.node.location[-1],
                      attachment_type=allure.attachment_type.PNG)


@pytest.fixture(scope='session', autouse=True)
def create_db_user(config):
    session = requests.Session()
    data = {
        "username": config['login'],
        "email": config['email'],
        "password": config['password'],
        "confirm": config['password'],
        "term": "y",
        "submit": "Register"
    }
    session.request('POST', f'{config["url"]}/reg', data=data)
    yield
    data = {
        "username": config['login'],
        "password": config['password'],
        "submit": "Login"
    }
    session.request('POST', f'{config["url"]}/login', data=data)
    session.request('GET', f'{config["url"]}/api/del_user/{config["login"]}', data=data)


def generate_user(dong=0):
    Faker.seed(dong)
    fake = Faker(['cs_CZ', 'en_GB', 'ru_RU'])
    user = ''
    email = ''
    while len(user) < 7 or len(user) > 15 or len(email) < 7:
        user = fake.user_name()
        email = fake.ascii_email()
        print(user)
    data = {
        'username': user,
        'email': email,
        'password': fake.credit_card_security_code()
    }
    return data


@pytest.fixture()
def user_fixture():
    return generate_user(random.randint(1, 1000))


@pytest.fixture(params=[1])
def parametrized_fixture_good(request):
    return request.getfixturevalue('user_fixture')


@pytest.fixture(params=[1, 2, 3, 4, 5, 6])
def parametrized_fixture_api_add_user(request):
    if request == 1:
        username, email, password = request.getfixturevalue('user_fixture')
        return username*3, email, password
    elif request == 2:
        username, email, password = request.getfixturevalue('user_fixture')
        return username, '', password
    elif request == 3:
        username, email, password = request.getfixturevalue('user_fixture')
        return username, email, None
    elif request == 4:
        username, email, password = request.getfixturevalue('user_fixture')
        return username[:4], email, password
    elif request == 5:
        username, email, password = request.getfixturevalue('user_fixture')
        return username, 'itsnotemail', password
    else:
        username, email, password = request.getfixturevalue('user_fixture')
        return username, 't@t.t', password
