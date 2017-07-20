from selenium.webdriver.support import expected_conditions as EC

from elements.locators import MainScreenLocators
from screens.base_screen import BaseScreen
from screens.category_screen import CategoryScreen


class MainScreen(BaseScreen):
    """ Main screen, screen contains a grid of possible categories user can browse"""

    def open_category(self, category_name):
        """
        Scrolls to the category name and opens it.
        :param category_name: the name of category, method make it titled
        :type category_name: str
        :return: CategoryScreen object
        """
        self.wait.until(EC.element_to_be_clickable(MainScreenLocators.TEXTVIEW))  # TODO maybe move it to init?
        element = self.driver.find_element_by_android_uiautomator(
            MainScreenLocators.CATEGORY_TEMPLATE.format(category_name.title()))
        element.click()
        return CategoryScreen(self.driver)
