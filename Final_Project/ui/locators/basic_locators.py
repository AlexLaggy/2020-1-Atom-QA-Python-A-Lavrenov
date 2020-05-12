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

    CHECK_SMTP_ICON = (By.XPATH, '//h1[contains(text(), "What Will the Internet Be Like in the Next 50 Years?"]')


class SegmentLocators:
    SEGMENT_MAIN = (By.XPATH, '//a[@class="center-module-button-cQDNvq center-module-segments-3y1hDo"]')

    SEGMENT_USER_LIST_PAGE = (By.XPATH, '//a[@href="/segments/users_list"]')

    SEGMENT_USER_LIST_SELECTOR = (By.XPATH, '//div[@class="select-module-item-3gX1Mz"]')

    SEGMENT_USER_LIST_SELECT_EMAILS = (By.XPATH, '//li[@data-test="emails"]')

    SEGMENT_USER_LIST_NAME = (By.ID, 'input_form_8')

    SEGMENT_USER_LIST_FILE_BUTTON = (By.XPATH, '//div[@data-test="buttonFile"]')

    SEGMENT_USER_LIST_UPLOAD = (By.XPATH, '//div[@data-test="buttonSubmit"]')

    SEGMENT_CREATE = (By.XPATH, '//div[@class="segments-list__btn-wrap js-create-button-wrap"]'
                                '//button[@class="button button_submit"]')

    SEGMENT_CREATE_AUDIT_SEGMENT = (By.XPATH, '//div[@class="create-segment-form__block '
                                              'create-segment-form__block_add js-add-segments-button"]')

    SEGMENT_CREATE_AUDIT_USER_LIST = (By.XPATH, '//div[contains(text(), "Списки пользователей")]')

    SEGMENT_CREATE_AUDIT_ADD_CHOOSE = (By.XPATH, '//div[@data-class-name="SourceView"]'
                                                 '//input[@class="adding-segments-source__checkbox'
                                                 ' js-main-source-checkbox"]')

    SEGMENT_CREATE_AUDIT_ADD = (By.XPATH, '//div[@class="adding-segments-modal__btn-wrap js-add-button"]'
                                          '//button[@class="button button_submit"]')

    SEGMENT_CREATE_AUDIT_NAME = (By.XPATH, '//div[@class="input input_create-segment-form"]'
                                           '//input[@type="text"]')

    SEGMENT_CREATE_BUTTON = (By.XPATH, '//div[@class="create-segment-form__btn-wrap js-create-segment-button-wrap"]'
                                       '//button[@class="button button_submit"]')

    # Check created
    SEGMENT_FIND_CREATED_NAME = (By.XPATH, '//input[@class="suggester-ts__input"]')

    SEGMENT_FIND_BY_NAME = (By.XPATH, f'//span[@title="AlexTest"]')

    SEGMENT_REMOVE = (By.XPATH, '//div[@class="remove-source-wrap js-remove-source"]')

    SEGMENT_REMOVE_CONFIRM = (By.XPATH, '//button[@class="button button_confirm-remove button_general"]')

    SEGMENT_WAIT = (By.XPATH, '//li[@data-id="_emptyItem"]')
