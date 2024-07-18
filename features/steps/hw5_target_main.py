from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver import Keys
from time import sleep
import time


@given('Open target main page')
def open_target_main_page(context):
    context.tic = time.time()
    context.driver.get('https://www.target.com/')

@when('Search for {product}')
def search_for_product(context, product):
    search_input = context.driver.find_element(By.ID, 'search')
    search_input.send_keys(product)
    search_input.send_keys(Keys.RETURN)