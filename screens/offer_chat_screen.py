from elements.chat_screen_elements import ChatField, ChatFieldMessage
from elements.locators import OfferChatScreenLocators
from screens.base_screen import BaseScreen


class OfferChatScreen(BaseScreen):
    """    """
    msg_to_send = ChatField()
    message = ChatFieldMessage()

    def verify_made_offer(self):
        assert "made an offer".upper() in self.message

    def send_message(self, text):
        """

        :param text:
        :return: None
        """
        self.msg_to_send = text
        self.wait_element_to_be_clickable(OfferChatScreenLocators.SEND_BTN)
        element = self.driver.find_element(*OfferChatScreenLocators.SEND_BTN)
        element.click()

    def leave_chat_offer(self):
        """

        :return: None
        """
        element = self.driver.find_element(*OfferChatScreenLocators.CANCEL_OFFER_BTN)
        element.click()

    def confirm_cancel_offer(self):
        """

        :return: None
        """
        element = self.driver.find_element(*OfferChatScreenLocators.CONFIRM_CANCEL_OFFER_BTN)
        element.click()

    def clenup_offer(self):
        """

        :return: None
        """
        self.send_message("Sorry, offer was made for testing purposes")
        self.leave_chat_offer()
        self.confirm_cancel_offer()

    def verify_cancelled_offer(self):
        pass
