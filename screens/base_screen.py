from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BaseScreen(object):
    """Base class to initialize the base screen that will be called from all screens"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def wait_element_to_be_clickable(self, locator):
        """Wrapper to wait elements"""
        self.wait.until(EC.element_to_be_clickable(locator))
