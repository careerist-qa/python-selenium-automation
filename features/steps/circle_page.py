from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from behave import given, then, when
from time import sleep


@given('Open Circle page')
def open_circle(context):
    context.app.circle_page.open_circle()


@given('Store original window')
def store_windows(context):
    context.windows = context.app.page.get_all_windows()
    context.original_window = context.app.page.get_current_window()
    # print('All windows', context.windows)
    # print('Current window', context.original_window)


@when('Click Google Play button')
def click_google_play(context):
    context.app.circle_page.click_google_play()


@when('Switch to new window')
def switch_window(context):
    context.app.page.switch_to_new_window()


@then('Verify that clicking though Circle tabs works')
def verify_can_click_tabs(context):
    context.app.circle_page.verify_can_click_tabs()


@then('Verify Google Play Target page opened')
def verify_google_play_opened(context):
    context.app.partner_page.verify_google_play_opened()


@then('Close current page')
def close(context):
    context.app.page.close_page()


@then('Return to original window')
def switch_to_original(context):
    context.app.page.switch_to_window(context.original_window)
