from selenium.webdriver.common.by import By
from behave import then

CART_TEXT = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")


@then('{text} is present')
def verify_result(context, text):
    #result_text = context.driver.find_element(*CART_TEXT).text
    #assert 'Your Shopping Cart is empty.' in result_text
    context.app.cart_result.verify_cart_text(text)
