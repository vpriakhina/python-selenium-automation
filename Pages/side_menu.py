from Pages.Base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class SideMenu(Page):
    MUSIC_MENU = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button")

    def click_music_menu(self):
        self.wait_for_element_click(*self.MUSIC_MENU)
        sleep(1)

    def verify_item_amount(self, expected_item_count: int):
        """
        Verifies amount of menu items
        :param expected_item_count: expected amount of menu items
        """
        actual_item = len(self.driver.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        assert actual_item == expected_item_count, f'Expected text {expected_item_count}, but got {actual_item}'