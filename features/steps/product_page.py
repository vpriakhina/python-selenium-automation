from selenium.webdriver.common.by import By
from behave import when

ADD_TO_CART_BUTTON = (By.ID, 'add-to-cart-button')
SIDE_CLOSE_BUTTON = (By.ID, 'attach-close_sideSheet-link')


@when('Click Add on cart button')
def click_add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BUTTON).click()


@when('Close suggestion side section')
def close_side_section(context):
    c_button = context.driver.find_elements(*SIDE_CLOSE_BUTTON)
    if len(c_button) == 1:
        c_button[0].click()
    else:
        pass
