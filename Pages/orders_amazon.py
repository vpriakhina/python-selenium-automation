from Pages.Base_page import Page
from selenium.webdriver.common.by import By


class OrderFunctionality(Page):

    def verify_signin(self, link):
        self.verify_link(link)