from selenium.webdriver.common.by import By

# TODO maye change locators name to lower?


class WelcomeScreenLocators(object):
    """A class for welcome screen locators. All welcome screen locators should come here."""

    EMAIL_BUTTON = (By.ID, "com.thecarousell.Carousell:id/email_signin_button")


class SignUpScreenLocators(object):
    """A class for sign up screen locators."""

    LOGIN_TAB = (By.XPATH, "//android.widget.TextView[@text='LOGIN']")


class LoginScreenLocators(object):
    """A class for login screen locators."""

    LOGIN_BTN = (By.ID, "com.thecarousell.Carousell:id/action_signin")


class MainScreenLocators(object):
    """A class for main screen locators."""

    TEXTVIEW = (By.XPATH, "//android.widget.TextView")
    CATEGORY_TEMPLATE = 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(' \
                        'new UiSelector().text("{}").instance(0));'


class CategoryScreenLocators(object):
    """A class for category screen locators."""

    PRODUCTS_LIST = (By.ID, "com.thecarousell.Carousell:id/grid_product")
    PRODUCTS = (By.ID, "com.thecarousell.Carousell:id/view_product")
    DIALOGUE_OK_BTN = (By.XPATH, "//android.widget.TextView[contains(@text, 'OK')]")


class ProductDetailedScreenLocators(object):
    """A class for product detailed screen locators."""

    DIALOGUE_OK_BTN = (By.XPATH, "//android.widget.TextView[contains(@text, 'OK')]")
    ASK_THE_SELLER_DAILOGUE_OK_BTN = (By.XPATH, "//android.widget.TextView[contains(@text, 'OK')]")
    BUY_BTN = (By.ID, "com.thecarousell.Carousell:id/button_buy")


class YourOfferScreenLocators(object):
    """A class for your offer screen locators."""

    SUBMIT_BTN = (By.ID, "com.thecarousell.Carousell:id/action_submit")
    CONFIRM_SUBMITTING_OFFER_BTN = (By.ID, "android:id/button1")
    DISMISS_SUBMITTING_OFFER_BTN = (By.ID, "android:id/button2")


class OfferChatScreenLocators(object):
    """A class for offer screen locators."""

    SEND_BTN = (By.ID, "com.thecarousell.Carousell:id/button_send")
    CANCEL_OFFER_BTN = (By.ID, "com.thecarousell.Carousell:id/button_chat_left")
    CONFIRM_CANCEL_OFFER_BTN = (By.ID, "android:id/button1")
    DISMISS_CANCEL_OFFER_BTN = (By.ID, "android:id/button2")
