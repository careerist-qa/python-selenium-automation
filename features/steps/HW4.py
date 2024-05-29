from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

#HOMEWORK 4.1
searched_product = (By.CSS_SELECTOR, "span.h-text-bs.h-display-flex.h-flex-align-center.h-text-grayDark.h-margin-l-x2")
search_box = (By.ID, 'search')
search_button = (By.CSS_SELECTOR, "button.styles__SearchButton-sc-wnzihy-3.SOItS")

@given('Open Target site')
def open_target_page(context):
    context.driver.get('https://www.target.com/')

@when('Input {product} into search bar')
def input_product(context, product):
    context.driver.find_element(*search_box).send_keys(product)
    context.driver.find_element(*search_button).click()
    sleep(2)

@then('Item results for {product} are displayed')
def product_results(context, product):
    assert (context.driver.find_element(*searched_product).text == product)
    print('TEST PASSED')


#HOMEWORK 4.2
benefit_cells = (By.CSS_SELECTOR, "div.cell-item-content")

@given('Open Target benefit page')
def open_page(context):
    context.driver.get('https://www.target.com/circle')
    sleep(2)

@then("10 Benefit cells populate")
def benefit_populate(context):
    benefit_amount = context.driver.find_elements(*benefit_cells)
    assert 10 == len(benefit_amount)
    print('EXACTLY TEN')


#HOMEWORK 4.3
add_cart = (By.XPATH, "//button[text()='Add to cart']")
add_cart2 = (By.XPATH, "//button[text()='Add to cart' and @data-test='orderPickupButton']")
zip_code = (By.CSS_SELECTOR, ".styles__ButtonPrimary-sc-5fh6rr-0.hCWYcY.bEdlr")
pick_pickup = (By.ID, "addToCartButtonOrTextIdFor14721821")
cart_button = (By.CSS_SELECTOR, "a[href='/cart?prehydrateClick=true']")
cart_filled = (By.CSS_SELECTOR, "div.h-padding-v-default")
go_cart = (By.XPATH, "//button[text()='Continue shopping']")

@when('Add any item to cart')
def add_item(context):
    sleep(4)
    context.driver.find_element(*add_cart).click()
    context.driver.find_element(*add_cart2).click()


@when("Go to cart")
def go_cart(context):
    sleep(2)
    context.driver.get('https://www.target.com/')
    context.driver.find_element(*cart_button).click()
    sleep(2)

@then('Verify an item is in cart')
def filled_cart(context):
    context.driver.find_element(*cart_filled).is_displayed()
    print('ITEM IS IN CART!')


