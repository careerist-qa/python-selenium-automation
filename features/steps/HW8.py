from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target help page')
def open_target_help_page(context):
    context.app.target_help_page.open_help_page()


@when('Select dropdown option')
def verify_dropdown_present(context):
    context.app.target_help_page.dropdown_present()


@then('Verify page is correctly changed')
def verify_page_is_correct(context):
    context.app.target_help_page.page_change()


@then('Enter username')
def enter_username(context):
    context.app.target_help_page.enter_user()


@then('Enter Password')
def enter_password(context):
    context.app.target_help_page.enter_pass()


@then('Click on sign in')
def click_sign_in(context):
    context.app.target_help_page.click_sign_in()


@then('Verify error message appears')
def verify_error_message(context):
    context.app.target_help_page.verify_error()
