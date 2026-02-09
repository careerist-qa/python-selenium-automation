from selenium.webdriver.common.by import By
from behave import given, when, then


@given("Open target main page")
def open_target_main_page(context):
    context.driver.get('https://www.target.com/')

