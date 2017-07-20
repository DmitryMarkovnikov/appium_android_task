from elements.locators import WelcomeScreenLocators
from screens.base_screen import BaseScreen
from screens.signup_screen import SignUpScreen


class WelcomeScreen(BaseScreen):
    """ Welcome screen class"""

    def use_email_to_enter(self):
        """

        :return: SignUpScreen object
        """
        self.wait_element_to_be_clickable(WelcomeScreenLocators.EMAIL_BUTTON)
        element = self.driver.find_element(*WelcomeScreenLocators.EMAIL_BUTTON)
        element.click()
        return SignUpScreen(self.driver)
