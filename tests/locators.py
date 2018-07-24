from selenium.webdriver.common.by import By


class MainPageLocators(object):
    LOGIN = (By.CLASS_NAME, "login-button")
    BLOG_LINK = (By.LINK_TEXT, "Blog")
    DOCUMENT_LINK = (By.LINK_TEXT, "Documents")


class LoginPageLocators(object):
    EMAIL = (By.ID, "id")
    PASSWORD = (By.ID, "passwd")
    LOGIN_BUTTON = (By.CLASS_NAME, "MdBtn03Login")


class DevConsoleLocators(object):
    PROVIDER_TITLE = (By.CLASS_NAME, "providerTitle")
    CREATE_PROVIDER_BUTTON = (By.CLASS_NAME, "Button-createProvider")


class BlogLocators(object):
    MENU_BLOG = (By.CLASS_NAME, "menu_blog")


class DocumentLocators(object):
    LINE_LOGIN_CARD = (By.ID, "IndexLineLogin")


class LINELoginDocumentLocators(object):
    IOS_TRY_LOGIN_LINK = (By.CSS_SELECTOR, 'a[href=\'/en/docs/line-login/ios/try-line-login\']')


