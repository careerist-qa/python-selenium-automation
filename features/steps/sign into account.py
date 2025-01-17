from selenium.webdriver.common.by import By
from behave import given, when, then


@when('user clicks on sign in button')
def sign_in(context):
    context.app.header.sign_in()

@when('user clicks on side navigation side in button')
def side_navigation(context):
    context.app.header.side_nav_sign_in()

@then('Verify if Sign in message is displayed')
def verify_sign_in(context):
    context.app.header.verify_sign_in_page()