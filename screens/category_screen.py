from elements.locators import CategoryScreenLocators
from screens.base_screen import BaseScreen
from screens.product_detailed_screen import ProductDetailedScreen


class CategoryScreen(BaseScreen):
    """Category screen contains a grid of possible products of this category"""

    def __init__(self, driver):
        """
        After initing the object screen closes dialogue screen and has products list
        """
        super(CategoryScreen, self).__init__(driver)
        self.close_dialogue_screen()
        self.wait_element_to_be_clickable(CategoryScreenLocators.PRODUCTS_LIST)
        self.products = self.driver.find_elements(*CategoryScreenLocators.PRODUCTS)

    def close_dialogue_screen(self):
        """
        Closes dialogue screen
        :return: None
        """
        self.wait_element_to_be_clickable(CategoryScreenLocators.DIALOGUE_OK_BTN)
        element = self.driver.find_element(*CategoryScreenLocators.DIALOGUE_OK_BTN)
        element.click()

    def open_detailed_item_by_index(self, index):
        """
        Opens the detailed product screen by index
        :param index: index of item in self.product list to open
        :type index: int
        :return: ProductDetailedScreen object
        """
        self.products[index].click()
        return ProductDetailedScreen(self.driver)
