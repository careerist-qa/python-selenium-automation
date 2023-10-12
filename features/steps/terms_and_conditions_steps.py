from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('Open Amazon T&C page')
def Open_Amazon_TC_page(context):
    context.app.terms_and_conditions_page.open_amazon_tc_page(context)

@when('Store original windows')
def store_original_window(context):
    context.original_window = context.app.terms_and_conditions_page.store_original_window()

@when('Click on Amazon Privacy Notice link')
def click_privacy_notice_link(context):
    context.app.terms_and_conditions_page.