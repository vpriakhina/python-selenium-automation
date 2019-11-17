from Pages.main_page import MainPage
from Pages.search_results_page import SearchResults
from Pages.cart_page import CartResult
from Pages.orders_amazon import OrderFunctionality
from Pages.product_page import Product
from Pages.side_menu import SideMenu

class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.cart_result = CartResult(self.driver)
        self.orders_amazon = OrderFunctionality(self.driver)
        self.side_menu = SideMenu(self.driver)
        self.product_page = Product(self.driver)
