from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[aria-label*='Add to cart']")
OPEN_CART_PAGE = (By.CSS_SELECTOR, "a[class*='ButtonSecondary']")
CART_SUMMARY = (By.CSS_SELECTOR, "span[class*='CartSummary']")
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test*='cartItem-title']")


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.')


@when("Search for {item}")
def search_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)


@when('Click on Add to Cart button')
def click_add_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(2)


@when('Open cart page')
def open_cart(context):
    context.driver.get('https://www.target.com/cart')
    sleep(3)


@then('Verify cart has correct product')
def verify_product_name(context):
    actual_name = context.driver.find_element(*CART_ITEM_TITLE).text
    expected_product_name = 'cups'
    assert expected_product_name in actual_name.lower(), f'Expected {expected_product_name} but got {actual_name}'


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context,amount):
    cart_summary = context.driver.find_element(*CART_SUMMARY).text
    assert amount in cart_summary, f'Expected {amount} items but got {cart_summary}'