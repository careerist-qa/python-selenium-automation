from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://amazon.com')
    sleep(2)
    context.driver.refresh()

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(), '& Orders')]").click()


@when('Search for table')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

