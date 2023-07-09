from selenium.webdriver.common.by import By
from behave import given, when, then


SIGNIN_HEADER = (By.XPATH, "//h1[@class='a-spacing-small']")
EMAIL = (By.ID, 'ap_email')


@then('Verify Sign In page opens')
def verify_signin_opens(context):
    context.app.sign_in_page.verify_signin_opens()
