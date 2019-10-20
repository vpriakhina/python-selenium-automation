from selenium.webdriver.common.by import By
from behave import when, then

INPUT_FIELD = (By.CSS_SELECTOR, "input#helpsearch")
GO_BUTTON = (By.CSS_SELECTOR, "input.a-button-input")


@when('Input {help_search_word} into help search field')
def input_search_word(context, help_search_word):
    search_help = context.driver.find_element(*INPUT_FIELD)
    search_help.clear()
    search_help.send_keys(help_search_word)


@when('Click on Go icon')
def click_go(context):
    context.driver.find_element(*GO_BUTTON).click()


@then('Verify that {result_search_word} text is present')
def verify_help_result(context, result_search_word):
    help_search_result = context.driver.find_element(By.CSS_SELECTOR, "div.help-content h1").text
    assert result_search_word in help_search_result, f"Expected text is product, but got {help_search_result}"
