from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

BENEFIT_LINK = (By.CSS_SELECTOR, "div.benefit-box")

@given('Open Amazon prime page')
def open_amazon_prime(context):
    context.driver.get('https://www.amazon.com/amazonprime')


@then('{expected_item_count} Prime membership benefits blocks are present')
def verify_amount_of_items(context, expected_item_count):
    sleep(3)
    actual_item_count = len(context.driver.find_elements(*BENEFIT_LINK))
    assert actual_item_count == int(expected_item_count), \
        f'Expected {expected_item_count} but got {actual_item_count}'