from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@then('Add product to cart')
def add_product_to_cart(context):
    context.driver.find_element(By.ID, 'add-to-cart-button').click()

