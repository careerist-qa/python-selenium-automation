from behave import given, when, then



@given('Open Amazon Page')
def open_amazon(context):
    # context.driver.get('https://www.amazon.com/')
    context.app.main_page.open_main()

@when('Click on Returns and Orders')
def click_returns_orders(context):
    # context.driver.find_element(By.ID, "nav-orders").click()
    context.app.header.click_orders()

@then('Verify Sign In page')
def sign_in_page(context):
    # context.driver.find_element(By.ID, "ap_email").click()
    context.app.signin_page.verify_signin_page()
