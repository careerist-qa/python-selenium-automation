from behave import given, when, then


@given('HW8 Open sign in page')
def open_sing_in_page(context):
    context.hw8app.hw8_page_login.open_target_sign_login_page()


@when('HW8 Store original window')
def store_original_window(context):
    context.original_window = context.hw8app.hw8_page_login.store_original_sign_in_page()
    # print(f'Stored original_window: {context.original_window}')


@when('HW8 Click on Target terms and conditions link')
def click_tc_link(context):
    context.hw8app.hw8_page_login.click_tc_link()


@when('HW8 Switch to the newly opened window')
def switch_to_tc_window(context):
    context.hw8app.hw8_page_login.switch_to_tc_window()