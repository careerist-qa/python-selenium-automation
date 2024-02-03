from selenium.webdriver.common.by import By
from behave import given, when, then

CART_HEADER = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(*CART_HEADER).text
    assert 'Your cart is empty' == actual_text, f"Expected 'Your cart is empty' but got {actual_text}"
