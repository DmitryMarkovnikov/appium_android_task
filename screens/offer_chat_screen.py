from elements.chat_screen_elements import ChatField, ChatFieldMessage
from elements.locators import OfferChatScreenLocators
from screens.base_screen import BaseScreen


class OfferChatScreen(BaseScreen):
    """  Offer chat screen, user can send and get message of possible offer  """
    msg_to_send = ChatField()
    message = ChatFieldMessage()

    def verify_made_offer(self):
        assert "made an offer".upper() in self.message, "Offer was not made"

    def send_message(self, text):
        """
        Send message to chat with provided text
        :param text: text to send
        :type text str
        :return: None
        """
        self.msg_to_send = text
        self.wait_element_to_be_clickable(OfferChatScreenLocators.SEND_BTN)
        element = self.driver.find_element(*OfferChatScreenLocators.SEND_BTN)
        element.click()

    def leave_chat_offer(self):
        """
        Click cancel offer button
        :return: None
        """
        element = self.driver.find_element(*OfferChatScreenLocators.CANCEL_OFFER_BTN)
        element.click()

    def confirm_cancel_offer(self):
        """
        Confirm offer cancellation
        :return: None
        """
        element = self.driver.find_element(*OfferChatScreenLocators.CONFIRM_CANCEL_OFFER_BTN)
        element.click()

    def clenup_offer(self):
        """
        Method that sends sorry message for the made offer and cancels the offer
        :return: None
        """
        self.send_message("Sorry, offer was made for testing purposes")
        self.leave_chat_offer()
        self.confirm_cancel_offer()
