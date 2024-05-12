from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from behave import given, when, then
from time import sleep

privacy_link = (By.CSS_SELECTOR, 'a[href="https://policies.google.com/privacy"]')


@given('Open Amazon T&C page')
def open_page(context):
    context.driver.get('https://www.aboutamazon.com/')


@when('Store original windows')
def store_window(context):
    context.window_handles = context.driver.current_window_handle


@when('Click on Amazon Privacy Notice link')
def click_privacy_link(context):
    context.driver.find_element(*privacy_link).click()


@when('Switch to the newly opened window')
def switch_to_window(context):
    context.driver.switch_to.window(context.driver.window_handles[1])
    sleep(2)


@then('Verify Amazon Privacy Notice page is opened')
def verify_privacy_notice(context):
    assert context.driver.current_window_handle == context.driver.window_handles[1]

@then('User can close new window and switch back to original')
def switch_to_original_window(context):
    context.driver.close()
    context.driver.switch_to.window(context.driver.window_handles[0])

