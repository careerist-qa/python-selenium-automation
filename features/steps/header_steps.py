from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


@when('Click Amazon Orders link')
def click_orders(context):
     context.app.header.click_orders_link()