from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from pages import sign_in_page


@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()


@when("Click Sign in")
def click_sign_in(context):
    context.app.sign_in_page.click_sign_in()


@then('From side nav menu, click Sign in')
def side_nav_sign_in_btn(context):
    context.app.sign_in_page.side_nav_sign_in_btn()


@then('Verify Sign in form opened')
def verify_sign_in_shown(context):
    context.app.base_page.verify_sign_in_shown('Sign into your Target account')
    sleep(8)
