from behave import given, when, then


@given('Open target main page by Page')
def open_target_main_page_by_pages(context):
    context.hw6app.hw6_main_page.open()


@when('Search input for coffee by Page')
def search_for_product_by_pages(context):
    context.hw6app.hw6_header_page.search()


@when('Click on Cart icon by Page')
def click_cart_icon_by_pages(context):
    context.hw6app.hw6_header_page.cart_click()
