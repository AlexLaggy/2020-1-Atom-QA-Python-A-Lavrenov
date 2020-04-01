from selenium.webdriver.common.by import By

# LOGIN
EMAIL_LOCATOR = (By.NAME, 'email')

PASSWORD_LOCATOR = (By.NAME, 'password')

LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, '//div[@class="responseHead-module-button-1BMAy4"]')

LOGIN_BUTTON_LOGIN_FORM = (By.XPATH, '//div[@class="authForm-module-button-2G6lZu"]')

# Advertising company
COMPANY_STATES = (By.XPATH, '//div[@class="select__item select__item_value js-select-button"]')

COMPANY_STATES_DELETED = (By.XPATH, '//li[@cid="view170"]')
# SKIPPED

COMPANY_CREATE = (By.XPATH, '//a[@class="campaigns-tbl-settings__button campaigns-tbl-settings__button_new"]')

COMPANY_TARGET = (By.XPATH, '//div[@class="column-list-item _traffic"]')

COMPANY_INPUT_URL = (By.XPATH, '//input[@data-gtm-id="ad_url_text"]')
# <div class="input input_campaign-name input_with-close" cid="view1004" data-class-name="Input">    <div class="input__clear js-input-clear"></div><div class="input__wrap"><input type="text" maxlength="255" class="input__inp js-form-element" data-translated-attr="placeholder" data-translated-lit="" data-loc-ru="" data-loc-en="" data-dictionary-attr-path="src/langs/global.dictionary.json" placeholder=""></div></div>
# <input type="text" maxlength="255" class="input__inp js-form-element" data-translated-attr="placeholder" data-translated-lit="" data-loc-ru="" data-loc-en="" data-dictionary-attr-path="src/langs/global.dictionary.json" placeholder="">
COMPANY_CLEAR_NAME = (By.XPATH, '//div[@class="input__clear js-input-clear"]')

COMPANY_INPUT_NAME = (By.XPATH, '//div[@class="input input_campaign-name input_with-close"]'
                                '//input[@class="input__inp js-form-element"]')

COMPANY_TIZER = (By.XPATH, '//div[@id="149"]')

COMPANY_HEADER = (By.XPATH, '//input[@data-gtm-id="banner_form_title"]')

COMPANY_TEXT = (By.XPATH, '//textarea[@data-gtm-id="banner_form_text"]')
# <div class="button-module-transparent-19j-VO button-module-gray-2zb_m1 mediaLibrary-module-deleteButton-39W7XA" title="" data-test="button-remove-all"><div class="mediaLibrary-module-removeAllButtonText-2aDbuE">Удалить все</div></div>
COMPANY_DELETE_EXISTS_IMG = (By.XPATH, '//div[@data-test="button-remove-all"]')

# div class="button-module-transparentTextWrapper-3WOejv"
COMPANY_CONFIRM_DELETE_EXISTS_IMG = (By.XPATH, '//div[@class="button-module-transparentTextWrapper-3WOejv"]')
# <input type="file" class="input__inp input__inp_file js-form-element" data-gtm-id="load_image_btn_90_75">
COMPANY_UPLOAD_JPG_PATH = (By.XPATH, '//input[@class="input__inp input__inp_file js-form-element"]')
# <button class="button button_general" cid="view2621" data-class-name="General"><div class="button__text">Загрузить 90 x 75</div></button>
COMPANY_UPLOAD_JPG_SEND = (By.XPATH, '//button[@class="button button_general" ]')
# class="image-cropper__save js-save"
COMPANY_CONFIRM_UPLOAD_JPG = (By.XPATH, '//input[@type="submit"]')  # ' ' to '.'

COMPANY_CONFIRM_UPLOAD_JPG_KOSTIL = (By.XPATH, '//div[@class="modal-view__body__x js-modal-view-x"]')
# <span class="js-banner-form-btn"><button data-service-readonly="true" class="button button_submit" cid="view2477" data-class-name="Submit"><div class="button__text">Добавить объявление</div></button></span>
COMPANY_CONFIRM_TIZER = (By.XPATH, '//span[@class="js-banner-form-btn"]')
# <div class="button__text">Создать кампанию</div>
COMPANY_CONFIRM_CREATE = (By.XPATH, '//div[@class="button__text" and contains(text(), "Создать кампанию")]')





# <a class="center-module-button-cQDNvq center-module-segments-3y1hDo" href="/segments" data-push-state="true" target="_self">Аудитории</a>
SEGMENT_MAIN = (By.XPATH, '//a[@class="center-module-button-cQDNvq center-module-segments-3y1hDo"]')

# Create audit list from emails
# <a data-push-state="true" href="/segments/users_list" class="left-nav__link"><span class="left-nav__text js-align-info-bubble">Списки пользователей</span><span class="left-nav__count js-nav-item-count">0</span></a>
SEGMENT_USER_LIST_PAGE = (By.XPATH, '//a[@href="/segments/users_list"]')

# <div class="select-module-item-3gX1Mz" style="max-width: 500px;"><span class="select-module-itemInner-1XVjd7">Список id пользователей — Одноклассники</span></div>
SEGMENT_USER_LIST_SELECTOR = (By.XPATH, '//div[@class="select-module-item-3gX1Mz"]')

# <li class="optionsList-module-option-25VJZx" data-test="emails" style="height: 32px; line-height: 32px;">Список емейлов</li>
SEGMENT_USER_LIST_SELECT_EMAILS = (By.XPATH, '//li[@data-test="emails"]')

# <input name="title" id="input_form_8" placeholder="" type="text" class="addUsersForm-module-inputLong-1_EDlM input-module-input-1xGLR8 input-module-input-1xGLR8" value="Новый список пользователей. 2020-04-01 17:59">
SEGMENT_USER_LIST_NAME = (By.ID, 'input_form_8')

# <div class="button-module-button-gYtDlg button-module-gray-2zb_m1 button-module-button-gYtDlg" title="" data-test="buttonFile"><div class="button-module-textWrapper-3LNyYP">Выбрать файл списка</div></div>1
SEGMENT_USER_LIST_FILE_BUTTON = (By.XPATH, '//div[@data-test="buttonFile"]')

# <div class="button-module-button-gYtDlg button-module-blue-1Bdz4L button-module-button-gYtDlg" title="" data-test="buttonSubmit"><div class="button-module-textWrapper-3LNyYP">Загрузить</div></div>
SEGMENT_USER_LIST_UPLOAD = (By.XPATH, '//div[@data-test="buttonSubmit"]')

# <div class="segments-list__btn-wrap js-create-button-wrap" data-service-readonly="true"><button class="button button_submit" cid="view1715" data-class-name="Submit"><div class="button__text">Создать сегмент</div></button></div>
SEGMENT_CREATE = (By.XPATH, '//div[@class="segments-list__btn-wrap js-create-button-wrap"]'
                            '//button[@class="button button_submit"]')

# <div class="create-segment-form__block create-segment-form__block_add js-add-segments-button"><span data-translated="Add audience segments..." data-loc-en="Add audience segments..." data-loc-ru="Добавить аудиторные сегменты..." data-dictionary-path="src/pages/segments/subpages/segmentsList/subpages/segment/modules/segmentForm/langs/segmentFormView.dictionary.json">Добавить аудиторные сегменты...</span></div>
SEGMENT_CREATE_AUDIT_SEGMENT = (By.XPATH, '//div[@class="create-segment-form__block '
                                          'create-segment-form__block_add js-add-segments-button"]')
# <input class="adding-segments-source__checkbox js-main-source-checkbox" type="checkbox">
# <div class="adding-segments-source" cid="view2500" data-class-name="SourceView"><div class="adding-segments-source__header  adding-segments-source__header_with-icon js-source-header-wrap"><input class="adding-segments-source__checkbox js-main-source-checkbox" type="checkbox"><div class="adding-segments-source__text-wrap"><div class="adding-segments-source__text-top"><div class="adding-segments-source__text-logic-type js-logic-type"></div><span class="js-source-name">Индивидуальный доход/B - Средний доход</span></div><div class="adding-segments-source__text-bottom-wrapper"><div class="adding-segments-source__text-bottom"><span class="adding-segments-source__src-id js-source-id">#48411</span><span class="js-settings-info __ribs-hidden"></span></div></div></div></div><div class="adding-segments-source__content-wrap adding-segments-source__content-wrap_segment js-source-settings-wrap _hide"></div>
# </div>
# <div class="adding-segments-item" cid="view2951" data-class-name="TypeItemView" title="">Списки пользователей</div>
SEGMENT_CREATE_AUDIT_USER_LIST = (By.XPATH, '//div[contains(text(), "Списки пользователей")]')

# <div class="adding-segments-source" cid="view8876" data-class-name="SourceView"><div class="adding-segments-source__header  adding-segments-source__header_with-icon js-source-header-wrap"><input class="adding-segments-source__checkbox js-main-source-checkbox" type="checkbox"><div class="adding-segments-source__text-wrap"><div class="adding-segments-source__text-top"><div class="adding-segments-source__text-logic-type js-logic-type"></div><span class="js-source-name">Test</span></div><div class="adding-segments-source__text-bottom-wrapper"><div class="adding-segments-source__text-bottom"><span class="adding-segments-source__src-id js-source-id">#9847753</span><span class="js-settings-info __ribs-hidden">Условие: нет в списке</span></div><div class="js-view-source-wrapper"><a class="adding-segments-source__view-source-wrapper-link" href="/segments/users_list?sourceId=9847753" target="_blank">Смотреть источник</a></div></div></div><div class="adding-segments-source__expand js-expanded"></div></div><div class="adding-segments-source__content-wrap adding-segments-source__content-wrap_remarketing_users_list js-source-settings-wrap _hide"></div>
# </div>
SEGMENT_CREATE_AUDIT_ADD_CHOOSE = (By.XPATH, '//div[@data-class-name="SourceView"]'
                                             '//input[@class="adding-segments-source__checkbox js-main-source-checkbox"]')

# <div class="adding-segments-modal__btn-wrap js-add-button"><button data-service-readonly="true" class="button button_submit" cid="view2407" data-class-name="Submit"><div class="button__text">Добавить сегмент</div></button></div>
SEGMENT_CREATE_AUDIT_ADD = (By.XPATH, '//div[@class="adding-segments-modal__btn-wrap js-add-button"]'
                                      '//button[@class="button button_submit"]')
# <div class="input input_create-segment-form" cid="view6014" data-class-name="Input"><div class="input__wrap"><input type="text" maxlength="60" class="input__inp js-form-element" data-translated-attr="placeholder" data-translated-lit="" data-loc-ru="" data-loc-en="" data-dictionary-attr-path="src/langs/global.dictionary.json" placeholder=""></div></div>
SEGMENT_CREATE_AUDIT_NAME = (By.XPATH, '//div[@class="input input_create-segment-form"]'
                                       '//input[@type="text"]')

# <div class="create-segment-form__btn-wrap js-create-segment-button-wrap"><button data-service-readonly="true" class="button button_submit" cid="view2073" data-class-name="Submit"><div class="button__text">Создать сегмент</div></button></div>
SEGMENT_CREATE_BUTTON = (By.XPATH, '//div[@class="create-segment-form__btn-wrap js-create-segment-button-wrap"]'
                                   '//button[@class="button button_submit"]')


# Check created
# <input class="suggester-ts__input" data-translated-attr="placeholder" data-translated-lit="Поиск по имени или id ..." data-loc-ru="Поиск по имени или id ..." data-loc-en="Поиск по имени или id ..." data-dictionary-attr-path="src/langs/global.dictionary.json" placeholder="Поиск по имени или id ..." maxlength="50" style="width: 300px">
SEGMENT_FIND_CREATED_NAME = (By.XPATH, '//input[@class="suggester-ts__input"]')

# <span class="suggester-ts__item__name" title="Новый аудиторный сегмент 2020-04-01 18:45AlexTest">Новый аудиторный сегмент 2020-04-01 18:45AlexTest</span>
# SEGMENT_FIND_CLICK = (By.XPATH, f'//span[@title="{}"]')

# <div class="remove-source-wrap js-remove-source" data-service-readonly="true"><span class="icon-cross"></span></div>
SEGMENT_REMOVE = (By.XPATH, '//div[@class="remove-source-wrap js-remove-source"]')

# <button class="button button_confirm-remove button_general" cid="view1108" data-class-name="General"><div class="button__text">Удалить</div></button>
SEGMENT_REMOVE_CONFIRM = (By.XPATH, '//button[@class="button button_confirm-remove button_general"]')






NO_RESULTS = (By.XPATH, '//p[contains(text(), "No results found.")]')

COMPREHENSIONS = (By.XPATH, '//span[@class="comment" and contains(text(), "comprehensions")]')

NO_SUCH_ELEMENT = (By.NAME, '2132132131231231231231231')


EVENTS = (By.XPATH, '//nav[@id="mainnav"]//a[@href="/events/" and contains(text(), "Events")]')
PYTHON_EVENTS = (By.XPATH, '//li[@id="events"]//a[@href="/events/python-events"]')
EURO_PYTHON = (By.XPATH, '//a[@href="/events/python-events/875/"]')

INTRODUCTION = (By.CLASS_NAME, 'introduction')
LEARN_MORE = (By.CLASS_NAME, 'readmore')
