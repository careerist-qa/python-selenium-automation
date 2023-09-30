from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page


@then('Verify Sign-in page is opened')
def verify_sign_in(context):
    context.app.sign_in_page.verify_sign_in()
    context.verify_partial_url('com/ap/signin?')
