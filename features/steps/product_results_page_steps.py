from selenium.webdriver.common.by import By
from behave import then, when
from time import sleep

TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_RESULT = (By.CSS_SELECTOR, "picture.s-aspect-ratio-flex-container img.s-image")


@when('Open the first product search result')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULT).click()


@then('Search results for {product} is shown')
def verify_result(context, product):
    result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    assert product in result_text, f"Expected text is product, but got {result_text}"
