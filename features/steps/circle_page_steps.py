from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open Circle page')
def open_circle_page(context):
    context.app.circle_page.open_circle()


@then('Verify that clicking though Circle tabs works')
def verify_can_click_thru_tabs(context):
    context.app.circle_page.verify_can_click_thru_tabs()

