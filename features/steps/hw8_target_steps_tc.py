from behave import given, when, then


@then('HW8 Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.hw8app.hw8_page_tc.verify_partial_url_tc()


@then('HW8 User can close new window and switch back to original')
def close_and_switch_to_original_window(context):
    context.hw8app.hw8_page_tc.close_tc_window()
    context.hw8app.hw8_page_tc.switch_to_signin_page_by_id(context.original_window)
    context.hw8app.hw8_page_login.verify_partial_url_signin('/login')