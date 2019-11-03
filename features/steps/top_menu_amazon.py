from selenium.webdriver.common.by import By
from behave import when, then

BEST_SELLER = (By.XPATH, "//div[@id='nav-xshop']/a[contains(@href, 'bestsellers')]")
PAGE_OPENED = (By.ID, 'zg_banner_text_wrapper')
TOP_MENU =(By.CSS_SELECTOR, "div#zg_tabs li")


@when('Click Best Sellers link')
def click_best_seller_link(context):
    context.driver.find_element(*BEST_SELLER).click()


@then('Verify user can loop through top menu')
def verify_page(context):

    top_menu_webelements = context.driver.find_elements(*TOP_MENU)
    for i in range(len(top_menu_webelements)):
        webelement = context.driver.find_elements(*TOP_MENU)[i]
        print(webelement.text)
        top_menu_name = webelement.text
        webelement.click()
        page_name = context.driver.find_element(*PAGE_OPENED).text
        assert top_menu_name in page_name, f"Expected {top_menu_name}, but got {page_name}"