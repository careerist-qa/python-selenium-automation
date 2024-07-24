from behave import given, when, then


@then('HW7 Verify the sign-in form opened')
def verify_sign_in_form_opened(context):
    context.hw7app.hw7_page_login.verify_login_form()


@when('HW7 Input email and password on SignIn page')
def input_email_and_password(context):
    context.hw7app.hw7_page_login.input_email_and_password()


@when('Click on Sign in on SignIn page')
def click_on_sign_in_button(context):
    context.hw7app.hw7_page_login.click_on_sign_in_button()


@then('Verify user is logged in (sign in form should disappear)')
def verify_user_is_logged_in(context):
    context.hw7app.hw7_page_main.verify_sign_in_form_disappear()
    context.hw7app.hw7_page_main.verify_sign_in_url_disappear()