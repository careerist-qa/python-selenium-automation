from selenium.webdriver.common.by import By
from behave import then

CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")


@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty_message(context):
    actual_text = context.driver.find_element(*CART_EMPTY_MSG).text
    expected_text = 'Your cart is empty'
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    # context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")