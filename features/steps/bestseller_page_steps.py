from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

LINKS = (By.CSS_SELECTOR, "class*='nav-tab-all_style_zg-tabs-li")

@given('Verify Bestsellers page is opened')
def verify_bestseller_page(context):
    context.app.bestseller_page.verify_bestsellers_page_open(context)
