from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
SEARCH_SUBMIT = (By.NAME, 'btnK')
NEW_WINDOW = (By.CSS_SELECTOR,"#GUID-8966E75F-9B92-4A2B-BFD5-967D57513A40__GUID-2C1DF364-8FA3-4387-BCDB-2A63B7C51B64")
PRIVACY_NOTICE_LINK = (By.CSS_SELECTOR,"a[href='https://www.amazon.com/privacy']")

@given('Open Amazon T&C page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original windows')
def click_store_original_window(context):
    context.driver.myorgwindow=context.driver.current_window_handle

@when('Click on Amazon Privacy Notice link')
def click_amazon_privacy_notice_link(context):
        context.driver.find_element(*PRIVACY_NOTICE_LINK).click()

        # context.driver.wait.until(EC.new_window_is_opened(amazon_empty_cart_open))

@when('Switch to the newly opened window')
def switch_new_open_window(context):
    new_window=context.driver.window_handles[1]
    context.driver.switch_to.window(new_window)

@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_notice_page(context):
   context.driver.find_element(*NEW_WINDOW)


@then('User can close new window')
def user_close_new_window(context):
    context.driver.close()


@then('switch back to original window')
def switch_back_original_window(context):
    original_window=context.driver.window_handles[0]
    context.driver.switch_to.window(context.driver.myorgwindow)
