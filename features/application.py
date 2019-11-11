from Pages.main_page import MainPage
from Pages.search_results_page import SearchResults
from Pages.cart_results import CartResult
from Pages.orders_amazon import OrderFunctionality


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.cart_result = CartResult(self.driver)
        self.orders_amazon = OrderFunctionality(self.driver)
