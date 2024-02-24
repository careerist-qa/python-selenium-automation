from selenium.webdriver.common.by import By
from behave import given, when, then


HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader']")


@given('Open Target main page')
def open_target_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main()


@when('Search for {product}')
def search_product(context, product):
    context.app.header.search_product()


@when('Click on Cart icon')
def click_cart(context):
    context.app.header.click_cart_icon()


@when('Hover over signin')
def hover_signin_btn(context):
    context.app.header.hover_signin_btn()


@then('Verify header in shown')
def verify_header(context):
    # header = context.driver.find_element(*HEADER)
    # print(header)
    context.driver.find_element(*HEADER)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount)
    header_links = context.driver.find_elements(*HEADER_LINKS)
    assert len(header_links) == expected_amount, f'Expected {expected_amount} links, but got {len(header_links)}'


@then('Verify signin arrow shown')
def verify_signin_arrow(context):
    context.app.header.verify_signin_arrow()
