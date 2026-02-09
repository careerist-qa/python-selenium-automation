
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
CART_SUMMARY = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")
BENEFIT_CELL = (By.CSS_SELECTOR, '[class="sc-3e90527f-1 colamC storycard--text"')
ADD_CART_BUTTON = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextIdFor"]')
ADD_CART_BUTTON_2 = (By.CSS_SELECTOR, '[aria-label="Fulfillment"] [id*="addToCartButtonOrTextId')
ADD_CART_BUTTON_3 = (By.CSS_SELECTOR, '[href="/cart"]')
CART_ITEM_TITLE = (By.CSS_SELECTOR, "[data-test='cartItem-title']")


@given('Open Target circle page')
def open_cart(context):
    context.driver.get('https://www.target.com/circle')
    sleep(3)


@then('Verify two storycards')
def verify_storycards(context):
    actual_storycards_len = context.driver.find_elements(*BENEFIT_CELL)
    print(f'Storycards: {len(actual_storycards_len)}')
    assert len(actual_storycards_len) == 2, f'Story cards count {len(actual_storycards_len)} should equal 2'


@when('Add item to cart')
def add_to_cart(context):
    sleep(10)
    context.driver.find_element(*ADD_CART_BUTTON).click()
    sleep(10)
    context.driver.find_element(*ADD_CART_BUTTON_2).click()
    sleep(5)
    context.driver.find_element(*ADD_CART_BUTTON_3).click()


@then('Verify {item} in cart')
def verify_product_name(context, item):
    sleep(5)
    product_name_in_cart = context.driver.find_element(*CART_ITEM_TITLE).text
    print('Name in cart: ', product_name_in_cart)
    assert item in product_name_in_cart.lower(), \
        f'Expected {item} did not match {product_name_in_cart}'



