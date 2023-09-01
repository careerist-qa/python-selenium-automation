from behave import given, when, then


@then('Verify sign in page opened')
def verify_signin_opened(context):
    context.app.signin_page.verify_signin_opened()
