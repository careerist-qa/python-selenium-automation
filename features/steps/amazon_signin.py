from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from selenium.webdriver.support import expected_conditions as EC



CLICK_ORDER = (By.CSS_SELECTOR,"a[href*='nav_or']")
CONFIRM_SIGNIN_PAGE = (By.CSS_SELECTOR,"form[name='signIn']")
EMAIL_ID_EXISTS = (By.CSS_SELECTOR,'input#ap_email')

#$$("form[name='signIn']")
#$$("input#ap_email")

@given('Open Amazon page')
def open_Amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on returns and order icon')
def click_returns_and_order(context ):
    order_button=context.driver.find_element(*CLICK_ORDER)
    context.driver.wait.until(EC.element_to_be_clickable(order_button))
    order_button.click()


@then('Sign in page is opened')
def verify_sign_in_page_open(context):
    context.driver.find_element(*CONFIRM_SIGNIN_PAGE)

@then('{search_word} Header is visible')
def verify_sign_in_header_visible(context,search_word):
    assert search_word.lower() in context.driver.current_url.lower(), \
        f'Expected query not in {context.driver.current_url.lower()}'
@then('Email field is exist')
def verify_email_field_exist(context):
    context.driver.find_element(*EMAIL_ID_EXISTS)




#$$("form[name='signIn']")
#$$("input#ap_email")

#ignIn']")
