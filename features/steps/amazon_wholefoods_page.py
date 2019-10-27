from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from behave import given, then

EXPECTED_SALE_TEXT = 'SALE'
LIST = (By.CSS_SELECTOR, "ul.s-result-list.s-col-3")


@given('Open Amazon Wholefoods page')
def open_product_page(context):
    context.driver.get('https://www.amazon.com/wholefoodsdeals')


@then('Verify Items have Regular price')
def regular_price_check(context):
    # searching for 2nd ul item with sale items
    top_list = context.driver.find_elements(*LIST)[1]

    # getting list of products from it
    items_list = top_list.find_elements_by_class_name("s-result-item")

    for product in items_list:
        sale = product.find_element_by_class_name('a-color-error')
        if EXPECTED_SALE_TEXT in sale.text:
            product_name = product.find_element_by_class_name('wfm-sales-item-card__product-name')
            regular = product.find_element_by_class_name('wfm-sales-item-card__regular-price')
            assert 'Regular' in regular.text and len(product_name.text) != 0
        else:
            raise Exception("No " + EXPECTED_SALE_TEXT + " found for " + product.text)
