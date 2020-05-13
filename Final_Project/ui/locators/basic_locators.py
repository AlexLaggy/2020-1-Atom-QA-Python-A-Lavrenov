from selenium.webdriver.common.by import By


class BaseLocators:
    EMAIL_LOCATOR = (By.ID, 'username')

    PASSWORD_LOCATOR = (By.ID, 'password')

    LOGIN_BUTTON_MAIN_PAGE = (By.ID, 'submit')

    LOGIN_CONTROLS_MAIN_PAGE = (By.ID, 'login-controls')


class RegLocators:
    GO_REG_BUTTON = (By.XPATH, '//a[@href="/reg"]')

    USERNAME_LOCATOR = (By.ID, 'username')

    EMAIL_LOCATOR = (By.ID, 'email')

    PASSWORD_LOCATOR = (By.ID, 'password')

    CONFIRM_PASSWORD_LOCATOR = (By.ID, 'confirm')

    CONFIRM_CITK_LOCATOR = (By.ID, 'term')

    SUBMIT_BUTTON_LOCATOR = (By.ID, 'submit')

    LOGIN_CONTROLS_MAIN_PAGE = (By.ID, 'login-controls')


class MainLocators:
    BUG_BUTTON = (By.CLASS_NAME, "uk-navbar-brand uk-hidden-small")

    HOME_BUTTON = (By.XPATH, '//a[contains(text(), "HOME")]')

    PYTHON_BUTTON = (By.XPATH, '//a[contains(text(), "Python")]')

    LINUX_BUTTON = (By.XPATH, '//a[contains(text(), "Linux")]')

    NETWORK_BUTTON = (By.XPATH, '//a[contains(text(), "Network")]')

    AREA_EXPANDED_LINUX = (By.XPATH, '//a[contains(text(), "Download Centos7")]')

    AREA_EXPANDED_NETWORK = (By.XPATH, '//a[contains(text(), "News")]')

    AREA_EXPANDED_PYTHON = (By.XPATH, '//a[contains(text(), "Flask")]')

    LENS_ICON = (By.XPATH, '//a[@href="https://www.popularmechanics.com/technology/'
                           'infrastructure/a29666802/future-of-the-internet/"]')

    LAPTOP_ICON = (By.XPATH, '//a[@href="https://en.wikipedia.org/wiki/Application_programming_interface"]')

    SMTP_ICON = (By.XPATH, '//a[@href="https://ru.wikipedia.org/wiki/SMTP"]')

    # CHECK_LENS_ICON = (By.XPATH, '//h1[contains(text(), "What Will the Internet Be Like in the Next 50 Years?"]')

    PYTHON_HISTORY = (By.XPATH, '//a[contains(text(), "Python history")]')

    PYTHON_FLASK = (By.XPATH, '//a[contains(text(), "About Flask")]')

    LINUX_DOWNLOAD = (By.XPATH, '//a[contains(text(), "Download Centos7")]')

    NETWORK_NEWS = (By.XPATH, '//a[contains(text(), "News")]')

    NETWORK_DOWNLOAD = (By.XPATH, '//a[@href="https://www.wireshark.org/#download"]')

    NETWORK_TCPDUMP = (By.XPATH, '//a[contains(text(), "Examples")]')
