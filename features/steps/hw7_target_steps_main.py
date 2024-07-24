from behave import given, when, then


@given('HW7 Open the main page')
def open_main_page(context):
    context.hw7app.hw7_page_main.open_target_home_page()


@when('HW7 Click the sign-in link')
def click_sign_in_link(context):
    context.hw7app.hw7_page_header.click_sign_in_link()
    context.hw7app.hw7_page_main.click_nav_sign_in_list()


@when('HW7 Search for {product}')
def search_for_product(context, product):
    context.hw7app.hw7_page_main.search_product(product)
