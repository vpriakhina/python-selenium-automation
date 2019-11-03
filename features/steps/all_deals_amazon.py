from selenium.webdriver.common.by import By
from behave import given, when, then

TODAYS_DEALS_HEADER = (By.CSS_SELECTOR, "div.suppleTitle h1[role = 'header']")


@then('{expected_header} are shown')
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*TODAYS_DEALS_HEADER).text
    assert actual_header == expected_header