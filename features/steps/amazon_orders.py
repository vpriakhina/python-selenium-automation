from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

ORDER_BUTTON = (By.XPATH, "//a[@id='nav-orders']/span[@class='nav-line-2']")
RESULTS_MESSAGE = (By.XPATH, "//div[@class='a-box-inner a-padding-extra-large']/h1")


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Order Button')
def click_button(context):
    context.driver.find_element(*ORDER_BUTTON).click()
    sleep(2)


@then('Result Contains {search_word}')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)
