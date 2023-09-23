from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, then

@then('Search christmas')
def item_search(context):
    context.driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox").send_keys('christmas')

@then('Click on Search')
def search_button (context):
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then("Goes to items page")
def items_page(context):
    context.driver.find_element(By.XPATH, "//img[@alt='Touchat Sherpa Green and Black Buffalo Plaid Christmas Twin Blanket, Fuzzy Fluffy Soft Cozy Blanket, Fleece Flannel Plush ...']").click()

@then("Adds the Item to Cart")
def add_item_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, ".add-to-cart-button").click()
    sleep(10)
@then("Checks their cart")
def checks_cart(context):
    context.driver.find_element(By.XPATH, "//a[@href='/cart?ref_=sw_gtc']").click()

#wait 10 seconds
sleep(10)