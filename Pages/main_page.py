from selenium.webdriver.common.by import By
from Pages.Base_page import Page
from selenium.webdriver.support.select import Select

class MainPage(Page):
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    CART_LINK = (By.CSS_SELECTOR, "a#nav-cart")
    ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
    HAM_MENU = (By.ID, 'nav-hamburger-menu')
    SELECT_DEPARTMENT = (By.CSS_SELECTOR, 'select.nav-search-dropdown')
    SELECT_DEPARTMENT_SPAN = (By.CSS_SELECTOR, '#nav-search-dropdown-card span.nav-search-label')

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_shop_cart(self):
        self.click(*self.CART_LINK)

    def click_amazon_orders(self):
        self.click(*self.ORDERS_LINK)

    def click_ham_menu(self):
        self.click(*self.HAM_MENU)

    def select_department_books(self):
        select_department_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department_element)
        select.select_by_value('search-alias=stripbooks')

    def select_department_electronics(self):
        select_department_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department_element)
        select.select_by_value('search-alias=electronics')

    def verify_selected_department(self, expected_department):
        self.verify_text(expected_department, *self.SELECT_DEPARTMENT_SPAN)


