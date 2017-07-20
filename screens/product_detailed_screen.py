from elements.locators import ProductDetailedScreenLocators
from screens.base_screen import BaseScreen
from screens.your_offer_screen import YourOfferScreen


class ProductDetailedScreen(BaseScreen):
    """ Product detailed screen, the detailed view of clicked product"""

    def __init__(self, driver):
        """
        After this screen opens there appeared two popups, init method closes all of them
        """
        super(ProductDetailedScreen, self).__init__(driver)
        self.close_dialogues_screen()

    def close_first_dialogue_screen(self):  # TODO change the name of method
        """
        Closes dialogue screen
        :return: None
        """
        self.wait_element_to_be_clickable(ProductDetailedScreenLocators.DIALOGUE_OK_BTN)
        element = self.driver.find_element(*ProductDetailedScreenLocators.DIALOGUE_OK_BTN)
        element.click()

    def close_second_dialogue_screen(self):  # TODO change the name of method
        """
        Closes dialogue screen
        :return: None
        """
        self.wait_element_to_be_clickable(ProductDetailedScreenLocators.ASK_THE_SELLER_DAILOGUE_OK_BTN)
        element = self.driver.find_element(*ProductDetailedScreenLocators.ASK_THE_SELLER_DAILOGUE_OK_BTN)
        element.click()

    def close_dialogues_screen(self):
        """
        Closes two screens
        :return: None
        """
        self.close_first_dialogue_screen()
        self.close_second_dialogue_screen()

    def buy_product(self):
        """
        Clicks buy button
        :return: YourOfferScreen object
        """
        element = self.driver.find_element(*ProductDetailedScreenLocators.BUY_BTN)
        element.click()
        return YourOfferScreen(self.driver)
