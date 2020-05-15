import pytest

from selenium.webdriver.support import expected_conditions as EC
from tests.base import BaseCase


class Test(BaseCase):

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_login(self):
        self.user_page.login()
        self.user_page.find(self.user_page.locators.LOGIN_CONTROLS_MAIN_PAGE, timeout=3)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_login_error(self):
        self.user_page.login(False)
        assert "Invalid username or password" in self.driver.page_source

    # @pytest.mark.skip("TEMP")
    @pytest.mark.UI
    @pytest.mark.parametrize('username,email,password', [('Artourchik', 'awp@top.co', 'p')])
    def test_login_status_after_registration(self, username, email, password):
        self.reg_page.click(self.reg_page.locators.GO_REG_BUTTON)
        self.reg_page.search(username, self.reg_page.locators.USERNAME_LOCATOR)
        self.reg_page.search(email, self.reg_page.locators.EMAIL_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.PASSWORD_LOCATOR)
        self.reg_page.search(password, self.reg_page.locators.CONFIRM_PASSWORD_LOCATOR)
        self.reg_page.click(self.reg_page.locators.CONFIRM_CITK_LOCATOR)
        self.reg_page.click(self.reg_page.locators.SUBMIT_BUTTON_LOCATOR)

        self.reg_page.find(self.reg_page.locators.LOGIN_CONTROLS_MAIN_PAGE, timeout=3)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

        user = self.db.session.query(self.db.table).filter(self.db.table.username == username).first()

        self.db.session.query(self.db.table).filter(self.db.table.username == username).delete()

        assert user.active == 1  # TODO: мы уже на странице, а следовательно статус в базе должен быть 1

    @pytest.mark.UI
    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.parametrize('username,email,password',
                             [('AutoSuccess', 'suc@t.tt', 't')])
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

        self.db.session.query(self.db.table).filter(self.db.table.username == username).delete()

    @pytest.mark.UI
    # @pytest.mark.skip(reason="TEMP")
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

        assert "Incorrect email" in self.driver.page_source  # TODO: должна быть ошибка, тк нету 1 буквы в расширении

    @pytest.mark.UI
    # @pytest.mark.skip(reason="TEMP")
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

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_bug(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.BUG_BUTTON)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_home(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.HOME_BUTTON)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_linux(self):
        self.user_page.login()

        self.main_page.find(self.main_page.locators.LINUX_BUTTON)
        self.main_page.find(self.main_page.locators.AREA_EXPANDED_LINUX)
        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_linux_download(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.LINUX_BUTTON)
        self.main_page.click(self.main_page.locators.LINUX_BUTTON)
        self.main_page.click(self.main_page.locators.LINUX_DOWNLOAD)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "Centos" in self.driver.page_source  # TODO: должен быть Centos, а там Fedora

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_network(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)
        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)
        self.main_page.find(self.main_page.locators.AREA_EXPANDED_NETWORK)

        assert "powered by ТЕХНОАТОМ" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_network_news(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)
        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)

        self.main_page.click(self.main_page.locators.NETWORK_NEWS)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "I have a lot of traffic" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_network_download(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)
        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)

        self.main_page.click(self.main_page.locators.NETWORK_DOWNLOAD)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "current stable release" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_network_tcpdump(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)
        self.main_page.click(self.main_page.locators.NETWORK_BUTTON)

        self.main_page.click(self.main_page.locators.NETWORK_TCPDUMP)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "troubleshooting" in self.driver.page_source

    # @pytest.mark.skip(reason="TEMP")
    @pytest.mark.UI
    def test_main_carousel_python_click(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.PYTHON_BUTTON)

        assert "powered by ТЕХНОАТОМ" in self.driver.page_source  # TODO: должен был открыться выпадающий список

    # @pytest.mark.skip(reason="WTF")
    @pytest.mark.UI
    def test_laptop_icon(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.LAPTOP_ICON)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "Wikipedia" in self.driver.page_source

    # @pytest.mark.skip(reason="WTF")
    @pytest.mark.UI
    def test_smtp_icon(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.SMTP_ICON)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "Wikipedia" in self.driver.page_source

    # @pytest.mark.skip(reason="WTF")
    @pytest.mark.UI
    def test_lens_icon(self):
        self.user_page.login()

        self.main_page.click(self.main_page.locators.LENS_ICON)

        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)

        assert "Will the Internet Be Like" in self.driver.page_source
