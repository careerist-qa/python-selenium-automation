from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open sign in page')
def open_sign_in_page(context):
    context.app.sign_in.open_sign_in()


@when('Store original window')
def store_original_window(context):
    context.original_window= context.app.sign_in.get_current_window_handle()


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions(context):
    context.app.sign_in.click_terms()


@when('Switch to the newly opened window')
def switch_to_newly_opened_window(context):
    context.app.sign_in.switch_to.window(context.driver.window_handle[1])


@when("user inputs correct email address")
def enter_email(context):
    context.app.sign_in.enter_email()


@when("User clicks continue button")
def continue_button(context):
    context.app.sign_in.click_continue()


@when("user enters incorrect password")
def enter_password(context):
    context.app.sign_in.enter_password()


@when("Clicks sign in with password")
def clicks_sign_in_password(context):
    context.app.sign_in.click_sign_in()



@then('Verify Terms and Conditions page is opened')
def verify_terms_and_conditions_page(context):
    context.app.terms_conditions_page.verify_terms()


@then('User can close new window')
def user_close_new_window(context):
    context.app.terms_conditions_page.close()


@then('switch back to original')
def switch_to_original_window(context):
    context.app.sign_in.switch_to_original_window(context.original_window)


@then("Verify error message is shown")
def verify_error_message(context):
    context.app.sign_in.verify_error_message()





