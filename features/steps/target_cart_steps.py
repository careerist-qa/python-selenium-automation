from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Click on Cart Icon')
def click_on_cart_icon(context):
        context.driver.find_element(By.XPATH, '//a[@data-test="@web/CartLink"]').click()


@then('"Your cart is empty" message is shown')
def verify_empty_cart_message(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(@class, styles_ndsHeading)]").text
    assert 'Your cart is empty' in actual_text, f"Expected 'Your cart is empty' text not in {actual_text}"


@when('Click on Sign In or Create Account button')
def sign_in_or_create_account_button(context):
   context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()


@then('"Sign in or create account" page is shown')
def verify_sign_in_message(context):
    actual_text = context.driver.find_element(By.XPATH,"//*[text()='Sign in or create account']")
    assert "Sign in or create account" in actual_text, f"Expected 'Sign in or create account' text not in {actual_text}"





