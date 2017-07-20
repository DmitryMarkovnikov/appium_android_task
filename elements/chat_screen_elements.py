from elements import BaseScreenTextElement


class ChatField(BaseScreenTextElement):
    locator = 'com.thecarousell.Carousell:id/text_chat'  # TODO maybe move it to locators package?


class ChatFieldMessage(BaseScreenTextElement):
    locator = 'com.thecarousell.Carousell:id/text_chat_action'  # TODO maybe move it to locators package?
