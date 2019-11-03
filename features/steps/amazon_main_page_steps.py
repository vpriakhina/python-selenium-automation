from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

ORDERS_LINK = (By.CSS_SELECTOR, "a#nav-orders span.nav-line-2")
SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
CART_LINK = (By.CSS_SELECTOR, "a#nav-cart")
HELP_LINK = (By.XPATH, "//li[@class='nav_last']/a[text()='Help']")
HAM_MENU = (By.ID, 'nav-hamburger-menu')
AMAZON_MUSIC_MENU_ITEM = (By.XPATH, "//ul[contains(@class, 'hmenu-visible')]//div[contains(text(), 'Amazon Music')]")
AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button")
CART_ITEM_COUNT = (By.ID, 'nav-cart-count')
DEALS_UNDER_25_LINK = (By.XPATH, "//a[contains(@aria-label, 'deals under $25')]")
PRODUCT_TO_CART = (By.ID, '103 50906b34-announce')


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


@when ('Store original windows')
def store_current_window(context):
    context.original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles


@when('Click to open Deals under 25')
def click_to_open_deals_under_25(context):
    context.driver.find_element(*DEALS_UNDER_25_LINK).click()


@when('Switch to the newly opened window')
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\ncurrent_windows\n', current_windows)

    new_windows = current_windows
    for old_windows in context.old_windows:
        new_windows.remove(old_windows)
    context.driver.switch_to_window(new_windows[0])


@then('Put any product into a cart')
def put_product_into_cart(context):
    context.driver.find_element(*PRODUCT_TO_CART).click()


@then('User can close new window and switch back to original')
def close_and_switch_window_back(context):
    context.driver.close()
    context.driver.switch_to_window(context.original_window)


@then('Refresh the page')
def page_refresh(context):
    context.driver.refresh()

