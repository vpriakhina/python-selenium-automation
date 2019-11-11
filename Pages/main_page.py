from selenium.webdriver.common.by import By
from Pages.Base_page import Page
from time import sleep

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    CART_LINK = (By.CSS_SELECTOR, "a#nav-cart")
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    MUSIC_MENU = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button")

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_shop_cart(self):
        self.click(*self.CART_LINK)

    def click_amazon_orders(self):
        self.click(*self.ORDERS_LINK)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)

    def click_music_menu(self):
        self.click(*self.MUSIC_MENU)

    def menu_item_count(self, expected_item):
        sleep(3)
        self.verify_item_count(expected_item, *self. AMAZON_MUSIC_MENU_ITEM_RESULTS)

