from elements import BaseScreenTextElement


class UsernameInputField(BaseScreenTextElement):
    locator = 'com.thecarousell.Carousell:id/text_username'  # TODO maybe move it to locators package?


class PasswordInputField(BaseScreenTextElement):
    locator = 'com.thecarousell.Carousell:id/text_password'  # TODO maybe move it to locators package?
