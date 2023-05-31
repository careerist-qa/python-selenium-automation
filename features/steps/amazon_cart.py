#$$("div.a-row.sc-your-amazon-cart-is-empty")
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


CLICK_CART = (By.CSS_SELECTOR,"span#nav-cart-count")
CONFIRM_EMPTY_PAGE = (By.CSS_SELECTOR,"div.a-row.sc-your-amazon-cart-is-empty")


#$$("form[name='signIn']")
#$$("input#ap_email")

@given('Click Amazon page')
def open_Amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on cart icon')
def click_cart(context ):
    order_button=context.driver.find_element(*CLICK_CART)
    context.driver.wait.until(EC.element_to_be_clickable(order_button))
    order_button.click()


@then('Amazon Empty Cart Page is opened')
def verify_amazon_empty_page_open(context):
   context.driver.find_element(*CONFIRM_EMPTY_PAGE)
    #context.driver.wait.until(EC.new_window_is_opened(amazon_empty_cart_open))





#$$("form[name='signIn']")
#$$("input#ap_email")

#ignIn']")
