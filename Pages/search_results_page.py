from Pages.Base_page import Page
from selenium.webdriver.common.by import By


class SearchResults(Page):
    TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")

    def verify_result_shown(self, expected_text):
        self.verify_text(expected_text, *self.TOOLBAR_TEXT_BOLD)


    def verify_link(self, link):
        self.verify_result(link, *self.EMAIL_FIELD)