class Page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://www.amazon.com/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, url=''):
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text == actual_text, f'Expected text {expected_text}, but got {actual_text}'

    def verify_result(self, text, *locator):
        result_text = self.driver.find_element(*locator).text
        assert text in result_text, f'Expected text {text}, but got {result_text}'

    def verify_link(self, link):
        assert link in self.driver.current_url

    def verify_item_count(self, expected_item, *locator):
        actual_item = len(self.driver.find_elements(*locator))
        assert actual_item == int(expected_item), f'Expected text {expected_item}, but got {actual_item}'

