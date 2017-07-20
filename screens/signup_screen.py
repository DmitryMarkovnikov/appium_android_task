from elements.locators import SignUpScreenLocators
from screens.base_screen import BaseScreen
from screens.login_screen import LoginScreen


class SignUpScreen(BaseScreen):
    """Sign up screen, here user can fill the form and sign up and switch to login tab """

    def sign_up(self):
        pass

    def switch_to_login(self):
        """

        :return:
        """
        self.wait_element_to_be_clickable(SignUpScreenLocators.LOGIN_TAB)
        element = self.driver.find_element(*SignUpScreenLocators.LOGIN_TAB)
        element.click()
        return LoginScreen(self.driver)
