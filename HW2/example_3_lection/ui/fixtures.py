import pytest

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from ui.pages.base import BasePage
from ui.pages.company import CompanyPage
from ui.pages.segment import SegmentPage
from ui.pages.user import UserPage
from api.client import ApiClient


class UsupportedBrowserException(Exception):
    pass
#
#
# @pytest.fixture(scope='function')
# def api_client(config):
#     return ApiClient(config['login'], config['password'])


@pytest.fixture(scope='function')
def base_page(driver):
    return BasePage(driver)


@pytest.fixture(scope='function')
def company_page(driver):
    return CompanyPage(driver)


@pytest.fixture(scope='function')
def segment_page(driver):
    return SegmentPage(driver)


@pytest.fixture(scope='function')
def user_page(driver, config):
    return UserPage(driver, config['login'], config['password'])


@pytest.fixture(scope='function')
def driver(config):
    browser = config['browser']
    version = config['version']
    selenoid = config['selenoid']
    url = config['url']
    download_dir = config['download_dir']

    if browser == 'chrome':
        options = ChromeOptions()
        options.add_argument("--window-size=800,600")

        prefs = {"download.default_directory": download_dir}
        options.add_experimental_option('prefs', prefs)
        if selenoid:
            capabilities = {'acceptInsecureCerts': True,
                            'browserName': 'chrome',
                            'version': version,
                            }
            driver = webdriver.Remote(command_executor=f'http://{selenoid}/wd/hub/',
                                      options=options,
                                      desired_capabilities=capabilities
                                      )
        else:
            manager = ChromeDriverManager(version=version)
            driver = webdriver.Chrome(executable_path=manager.install(),
                                      options=options,
                                      desired_capabilities={'acceptInsecureCerts': True}
                                      )
    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()
    yield driver
    driver.close()


@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def all_drivers(config, request):
    browser = request.param
    url = config['url']

    if browser == 'chrome':
        manager = ChromeDriverManager(version='latest')
        driver = webdriver.Chrome(executable_path=manager.install())

    elif browser == 'firefox':
        manager = GeckoDriverManager(version='latest')
        driver = webdriver.Firefox(executable_path=manager.install())

    else:
        raise UsupportedBrowserException(f'Usupported browser: "{browser}"')

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.close()
