from elements.login_screen_elements import UsernameInputField, PasswordInputField
from elements.locators import LoginScreenLocators
from screens.base_screen import BaseScreen
from screens.main_screen import MainScreen


class LoginScreen(BaseScreen):
    """Log in screen, here user can fill the form and login"""

    username = UsernameInputField()
    password = PasswordInputField()

    def login(self, account):
        """

        :return:
        """
        self.username = account["name"]
        self.password = account["password"]
        element = self.driver.find_element(*LoginScreenLocators.LOGIN_BTN)
        element.click()
        return MainScreen(self.driver)
