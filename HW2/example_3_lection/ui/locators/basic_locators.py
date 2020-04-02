from selenium.webdriver.common.by import By


class BaseLocators:
    EMAIL_LOCATOR = (By.NAME, 'email')

    PASSWORD_LOCATOR = (By.NAME, 'password')

    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, '//div[@class="responseHead-module-button-1BMAy4"]')

    LOGIN_BUTTON_LOGIN_FORM = (By.XPATH, '//div[@class="authForm-module-button-2G6lZu"]')


class CompanyLocators:
    # Advertising company
    COMPANY_STATES = (By.XPATH, '//div[@class="select__item select__item_value js-select-button"]')

    COMPANY_STATES_DELETED = (By.XPATH, '//li[@cid="view170"]')
    # SKIPPED

    COMPANY_CREATE = (By.XPATH, '//a[@class="campaigns-tbl-settings__button campaigns-tbl-settings__button_new"]')

    COMPANY_TARGET = (By.XPATH, '//div[@class="column-list-item _traffic"]')

    COMPANY_INPUT_URL = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')

    COMPANY_CLEAR_NAME = (By.XPATH, '//div[@class="input__clear js-input-clear"]')

    COMPANY_INPUT_NAME = (By.XPATH, '//div[@class="input input_campaign-name input_with-close"]'
                                    '//input[@class="input__inp js-form-element"]')

    COMPANY_TIZER = (By.XPATH, '//div[@id="149"]')

    COMPANY_HEADER = (By.XPATH, '//input[@data-gtm-id="banner_form_title"]')

    COMPANY_TEXT = (By.XPATH, '//textarea[@data-gtm-id="banner_form_text"]')

    COMPANY_DELETE_EXISTS_IMG = (By.XPATH, '//div[@data-test="button-remove-all"]')

    COMPANY_CONFIRM_DELETE_EXISTS_IMG = (By.XPATH, '//div[@class="button-module-transparentTextWrapper-3WOejv"]')

    COMPANY_UPLOAD_JPG_PATH = (By.XPATH, '//input[@class="input__inp input__inp_file js-form-element"]')

    COMPANY_UPLOAD_JPG_SEND = (By.XPATH, '//button[@class="button button_general" ]')

    COMPANY_CONFIRM_UPLOAD_JPG = (By.XPATH, '//input[@type="submit"]')  # ' ' to '.'

    COMPANY_CONFIRM_UPLOAD_JPG_KOSTIL = (By.XPATH, '//div[@class="modal-view__body__x js-modal-view-x"]')

    COMPANY_CONFIRM_TIZER = (By.XPATH, '//span[@class="js-banner-form-btn"]')

    COMPANY_CONFIRM_CREATE = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать кампанию")]')


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

    SEGMENT_REMOVE = (By.XPATH, '//div[@class="remove-source-wrap js-remove-source"]')

    SEGMENT_REMOVE_CONFIRM = (By.XPATH, '//button[@class="button button_confirm-remove button_general"]')
