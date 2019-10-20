from selenium.webdriver.common.by import By
from behave import then

EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")


@then('Verify Sign In page is opened')
def verify_signin_opened(context):
    context.driver.find_element(*EMAIL_FIELD)
    assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
