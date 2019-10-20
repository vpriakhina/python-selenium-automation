from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CART_LINK = (By.CSS_SELECTOR, "a#nav-cart")
HELP_LINK = (By.XPATH, "//li[@class='nav_last']/a[text()='Help']")
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button")
CART_ITEM_COUNT = (By.ID, 'nav-cart-count')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Amazon Orders link')
def click_orders_link(context):
    context.driver.find_element(*ORDERS_LINK).click()


@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()


@when('Click on Shopping Cart link')
def click_cart_link(context):
    context.driver.find_element(*CART_LINK).click()


@when('Click on Help link')
def click_help_link(context):
    context.driver.find_element(*HELP_LINK).click()


@when('Click on hamburger menu')
def click_ham_menu(context):
    context.driver.find_element(*HAM_MENU).click()


@when('Click on Amazon Music menu item')
def click_amazon_music(context):
    context.driver.find_element(*AMAZON_MUSIC_MENU_ITEM).click()


@then('{expected_item_count} menu items are present')
def verify_amount_of_items(context, expected_item_count):
    sleep(3)
    actual_item_count = len(context.driver.find_elements(*AMAZON_MUSIC_MENU_ITEM_RESULTS))
    assert actual_item_count == int(expected_item_count), \
        f'Expected {expected_item_count} but got {actual_item_count}'


@then('Verify cart has {expected_item_count} item')
def verify_result(context, expected_item_count):
    sleep(3)
    actual_items = context.driver.find_element(*CART_ITEM_COUNT).text
    assert actual_items == expected_item_count, f"Expected (expected_item_count), but got {actual_items}"
