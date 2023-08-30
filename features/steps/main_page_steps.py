from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
ORDERS_BTN = (By.ID, 'nav-orders')
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescItem')
HEADER_lINKS = (By.CSS_SELECTOR, "#zg_header a")
SIGNIN_BTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')
    sleep(2)
    context.driver.refresh()

@given('Open Amazon BestSeller page')
def open_amazon_bestseller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')


@when('Search for {product}')
def search_on_amazon(context, product):
    context.driver.find_element(*SEARCH_FIELD).send_keys(product)
    context.driver.find_element(*SEARCH_BTN).click()


@when('Click Orders')
def click_orders(context):
    context.driver.find_element(*ORDERS_BTN).click()


@when('Click on the cart icon')
def click_on_the_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '#nav-cart-count').click()


@then('Verify that your cart is empty')
def verify_that_your_cart_is_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')


@then('Verify many links are shown in the footer')
def verify_many_links(context):
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) > 1, f'Expected at least 2 links, but got {len(links)}'


@then('Verify many links are shown in the header')
def verify_many_links_header(context):
    links = context.driver.find_elements(*HEADER_lINKS)
    assert len(links) > 1, f'Expected at least 2 links, but got {len(links)}'


@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'


@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(SIGNIN_BTN),
        message='SignIn btn from popup not clickable'
    ).click()