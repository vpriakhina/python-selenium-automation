from Pages.Base_page import Page
from selenium.webdriver.common.by import By


class CartResult(Page):
    CART_TEXT = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")

    def verify_cart_text(self, text):
        self.verify_result(text, *self.CART_TEXT)
