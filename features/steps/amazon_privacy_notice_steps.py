from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


Privacy_Notice = (By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")


@given('Open Amazon T&C page')
def open_amazon_tc_page(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')


@when('Store original window')
def store_original_window(context):
    context.app.privacy_notice_page.store_original_window()


@when('Click on Amazon Privacy Notice link')
def click_on_amazon_privacy_notice_link(context):
    context.driver.find_element(*Privacy_Notice).click()


@when('Switch to the newly opened window')
def switch_to_the_newly_opened_window(context):
    context.app.privacy_notice_page.switch_to_the_newly_opened_window()


@then('Verify Amazon Privacy Notice page is opened')
def verify_amazon_privacy_notice_page_is_open(context):
    context.app.privacy_notice_page.verify_amazon_privacy_notice_page_is_open()


@then('User can close new window and switch back to original')
def user_can_close_new_window_and_switch_back_to_original(context):
    context.app.privacy_notice_page.get_current_window()