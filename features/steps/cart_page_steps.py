from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep



@then('Verify cart is Empty')
def empty_cart_verify(context):
    actual_result = 'Amazon Cart is em'
    expected_result = context.driver.find_element(By.XPATH, "//*[contains(text(), ' Amazon Cart is em')]" )
    assert actual_result == expected_result, f'expected assertion error {actual_result} should not equal {expected_result}'


@when('Click Cart')
def open_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class=nav-line-2][aria-hidden=true").click()

@then('Verify product is added to cart')
def check_product_added(context):
    actual_result = 'Added to Cart'
    expected_result = context.driver.find_element(By.XPATH, "//*[contains(text(), ' Added to Cart')]")
    assert actual_result == expected_result, f'expected assertion error {actual_result} should not equal {expected_result}'