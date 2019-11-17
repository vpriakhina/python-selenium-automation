from selenium.webdriver.common.by import By
from behave import given, then, when


TOOLBAR_TEXT_BOLD = (By.CSS_SELECTOR, "h1 span.a-text-bold")
PRODUCT_RESULT = (By.CSS_SELECTOR, "img.s-image")
COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div#variation_color_name span.selection")


@when('Open the first product search result')
def click_first_result(context):
    context.driver.find_element(*PRODUCT_RESULT).click()


@then('Search results for {product} is shown')
def verify_result(context, product):
    # result_text = context.driver.find_element(*TOOLBAR_TEXT_BOLD).text
    # assert product in result_text, f"Expected text is product, but got {result_text}"
    context.app.search_results_page.verify_result_shown(product)


@given('Open product {productid} page')
def open_product_page(context, productid):
    context.driver.get(f'https://www.amazon.com/gp/product/{productid}/')


@then('Verify user can loop though product colors')
def verify_colors(context):
    expected_colors = ['Black', 'Emerald', 'Ivory', 'Navy']
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        assert actual_color == expected_colors[color_webelements.index(color)]


@then('Verify user can select though product colors')
def verify_colors(context):
    expected_colors = ['Medium Wash', 'Dark Wash', 'Rinse']
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text
        assert actual_color == expected_colors[color_webelements.index(color)]

#===================================================================


@given('Open Amazon product {product_id} page')
def open_product(context, product_id):
    context.app.product_page.open_product(product_id)


@when('Hover over Add to Cart button')
def hover_add_to_cart(context):
    context.app.product_page.hover_add_to_cart()


@when('Hover over Sales and Deals button')
def hover_sales_and_deals(context):
    context.app.product_page.hover_sales_and_deals()


@then('Verify size selection tooltip is shown')
def verify_size_tooltip(context):
    context.app.product_page.verify_size_tooltip()


@then('Verify user sees the deals')
def verify_deals_present(context):
    context.app.product_page.verify_deals_present()