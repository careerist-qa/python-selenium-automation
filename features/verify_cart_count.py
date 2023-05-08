from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Go to keyboard item page")
def nav_keyboard_page(context):
    context.driver.get("https://www.amazon.com/AmazonBasics-Matte-Keyboard-QWERTY-Layout"
                       "/dp/B07WJ5D3H4/ref=sr_1_1_sspa?crid=1FVNUV7XN2ZHG&keywords=keyboard"
                       "&qid=1683507854&sprefix=keyboard%2Caps%2C353&sr=8-1-spons&psc=1&spLa="
                       "ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRjY3T0lLSTZNS04wJmVuY3J5cHRlZElkPUEwMTcxO"
                       "Dg2MURDVzExVlZURTFXNyZlbmNyeXB0ZWRBZElkPUEwNDcwNjgzMUVIMlk5MUZSVzMwUSZ"
                       "3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")


@when("Click add to cart button")
def add_keyboard(context):
    context.driver.find_element(By.ID, "add-to-cart-button").click()


@then("Verify added to cart")
def verify_one_in_cart(context):
    expected_text = "1"
    actual_text = context.driver.find_element(By.ID, "nav-cart-count").text()
    assert expected_text == actual_text, "Error: Nothing was added to the cart"
    








