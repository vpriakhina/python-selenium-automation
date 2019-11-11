from selenium.webdriver.common.by import By
from behave import then

#EMAIL_FIELD = (By.CSS_SELECTOR, "input[type='email']")


@then('Check {link} is opened')
def verify_signin_opened(context, link):
    # context.driver.find_element(*EMAIL_FIELD)
    # assert 'https://www.amazon.com/ap/signin' in context.driver.current_url
    context.app.orders_amazon.verify_signin(link)
