from elements.locators import YourOfferScreenLocators
from screens.base_screen import BaseScreen
from screens.offer_chat_screen import OfferChatScreen


class YourOfferScreen(BaseScreen):
    """ Screen where user can set the amount of money for that offer and submit it"""

    def submit(self):
        """
        Clicks the submit button
        :return: None
        """
        element = self.driver.find_element(*YourOfferScreenLocators.SUBMIT_BTN)
        element.click()

    def confirm_order(self):
        """
        Confirms sumbitting offer in pop up window
        :return: OfferChatScreen object
        """
        self.wait_element_to_be_clickable(YourOfferScreenLocators.CONFIRM_SUBMITTING_OFFER_BTN)
        element = self.driver.find_element(*YourOfferScreenLocators.CONFIRM_SUBMITTING_OFFER_BTN)
        element.click()
        return OfferChatScreen(self.driver)

    def dismiss_order(self):
        """
        Cancels sumbitting offer in pop up window
        :return: None
        """
        element = self.driver.find_element(*YourOfferScreenLocators.DISMISS_SUBMITTING_OFFER_BTN)
        element.click()

    def go_chating(self):
        """
        Wraps submitting and confirmation of offer
        :return: OfferChatScreen object
        """
        self.submit()
        return self.confirm_order()
