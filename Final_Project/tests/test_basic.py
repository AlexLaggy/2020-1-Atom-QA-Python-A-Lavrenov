import pytest
import time

from selenium.webdriver.support import expected_conditions as EC
from tests.base import BaseCase


class Test(BaseCase):

    @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_login(self):
        self.user_page.login()
        self.user_page.find(self.user_page.locators.LOGIN_CONTROLS_MAIN_PAGE, timeout=3)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_login_error(self):
        self.user_page.login(False)
        assert "Invalid username or password" in self.driver.page_source

    @pytest.mark.UI
    @pytest.mark.skip(reason="TEMP")
    @pytest.mark.parametrize('username,email,password',
                             [('AutoTest', 't@t.tt', 't')])
    def test_registry_success(self, username, email, password):
        self.reg_page.click(self.reg_page.locators.GO_REG_BUTTON)
        self.reg_page.search(username, self.reg_page.locators.USERNAME_LOCATOR)
        self.reg_page.search(email, self.reg_page.locators.EMAIL_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.PASSWORD_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.CONFIRM_PASSWORD_LOCATOR)
        self.reg_page.click(self.reg_page.locators.CONFIRM_CITK_LOCATOR)
        self.reg_page.click(self.reg_page.locators.SUBMIT_BUTTON_LOCATOR)

        self.reg_page.find(self.reg_page.locators.LOGIN_CONTROLS_MAIN_PAGE, timeout=3)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    @pytest.mark.UI
    @pytest.mark.skip(reason="TEMP")
    @pytest.mark.parametrize('username,email,password',
                             [('AutoTest2', 'tasdf@t.t', 't')])
    def test_registry_error_country_email(self, username, email, password):
        self.reg_page.click(self.reg_page.locators.GO_REG_BUTTON)
        self.reg_page.search(username, self.reg_page.locators.USERNAME_LOCATOR)
        self.reg_page.search(email, self.reg_page.locators.EMAIL_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.PASSWORD_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.CONFIRM_PASSWORD_LOCATOR)
        self.reg_page.click(self.reg_page.locators.CONFIRM_CITK_LOCATOR)
        self.reg_page.click(self.reg_page.locators.SUBMIT_BUTTON_LOCATOR)

        # Should take an error, bec. of a format of an email
        assert "Incorrect email" in self.driver.page_source

    @pytest.mark.UI
    @pytest.mark.skip(reason="TEMP")
    @pytest.mark.parametrize('username,email,password',
                             [('Auto', 'tasdf@t.tt', 't')])
    def test_registry_error_length_username(self, username, email, password):
        self.reg_page.click(self.reg_page.locators.GO_REG_BUTTON)
        self.reg_page.search(username, self.reg_page.locators.USERNAME_LOCATOR)
        self.reg_page.search(email, self.reg_page.locators.EMAIL_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.PASSWORD_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.CONFIRM_PASSWORD_LOCATOR)
        self.reg_page.click(self.reg_page.locators.CONFIRM_CITK_LOCATOR)
        self.reg_page.click(self.reg_page.locators.SUBMIT_BUTTON_LOCATOR)

        assert "Incorrect username" in self.driver.page_source

    @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel(self):
        self.user_page.login()
        # self.main_page.click(self.main_page.locators.BUG_BUTTON)
        # assert "powered by ТЕХНОАТОМ" in self.driver.page_source

        self.main_page.click(self.main_page.locators.HOME_BUTTON)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

        self.main_page.find(self.main_page.locators.LINUX_BUTTON)
        self.main_page.find(self.main_page.locators.AREA_EXPANDED_LINUX)

        self.main_page.click(self.main_page.locators.LINUX_BUTTON)
        self.main_page.click(self.main_page.locators.LINUX_BUTTON)
        self.main_page.find(self.main_page.locators.AREA_EXPANDED_LINUX)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)
        self.main_page.find(self.main_page.locators.AREA_EXPANDED_NETWORK)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

        self.main_page.find(self.main_page.locators.PYTHON_BUTTON)
        self.main_page.find(self.main_page.locators.AREA_EXPANDED_PYTHON)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_python_click(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.PYTHON_BUTTON)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    @pytest.mark.skip(reason="WTF")
    @pytest.mark.UI
    def test_laptop_icon(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.LAPTOP_ICON)
        time.sleep(2)
        assert "Application" in self.driver.page_source

    @pytest.mark.skip(reason="WTF")
    @pytest.mark.UI
    def test_smtp_icon(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.SMTP_ICON)
        time.sleep(2)
        assert "SMTP" in self.driver.page_source

    @pytest.mark.skip(reason="WTF")
    @pytest.mark.UI
    def test_lens_icon(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.LENS_ICON)
        self.main_page.find(self.main_page.locators.CHECK_SMTP_ICON, timeout=5)
        assert "Flat is better" in self.driver.page_source

