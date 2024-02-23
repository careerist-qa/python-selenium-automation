from behave import given, when, then


@given('Open Circle page')
def open_circle_page(context):
    context.app.circle_page.open_circle()


@given('Store original window')
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    # print('Current window', context.original_window)
    # print('All windows:', context.driver.window_handles)


@when('Click Google Play button')
def click_google_play_btn(context):
    context.app.circle_page.click_google_play_btn()


@when('Switch to new window')
def switch_to_new_window(context):
    context.app.circle_page.switch_to_new_window()
    # print('After switching to a new window:')
    # print('All windows:', context.driver.window_handles)
    # print('Current window', context.driver.current_window_handle)


@then('Verify Google Play Target page opened')
def verify_google_play_opened(context):
    context.app.circle_page.verify_google_play_opened()


@then('Close current page')
def close(context):
    context.driver.close()


@then('Return to original window')
def switch_to_original_window(context):
    context.app.circle_page.switch_to_window_by_id(context.original_window)
    # print('After switching back:')
    # print('Current window', context.driver.current_window_handle)


@then('Verify that clicking though Circle tabs works')
def verify_can_click_thru_tabs(context):
    context.app.circle_page.verify_can_click_thru_tabs()
