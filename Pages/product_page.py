from Pages.Base_page import Page
from selenium.webdriver.common.by import By


class Product(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    SIZE_SELECTION_TOOLTIP = (By.ID, 'a-popover-content-1')
    SALES_DEALS_BTN = (By.CSS_SELECTOR, "a[href*='sales-and-deals']")
    MUST_SEE_DEALS = (By.XPATH, "//h3[contains(text(),'Must-See')]")

    def open_product(self, product_id):
        # https://www.amazon.com/dp/B074TBCSC8
        self.open_page(f'dp/{product_id}')

    def hover_add_to_cart(self):
        cart_button = self.find_element(*self.ADD_TO_CART_BTN)
        self.actions.move_to_element(cart_button).perform()

    def verify_size_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_SELECTION_TOOLTIP)

    def hover_sales_and_deals(self):
        menu_button = self.find_element(*self.SALES_DEALS_BTN)
        self.actions.move_to_element(menu_button).perform()

    def verify_deals_present(self):
        self.wait_for_element_appear(*self.MUST_SEE_DEALS)