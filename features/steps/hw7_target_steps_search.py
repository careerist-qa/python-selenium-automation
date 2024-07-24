from behave import given, when, then


@when('HW7 Open the first product page')
def open_1st_product_detail_page(context):
    context.hw7app.hw7_page_search.open_the_first_product_in_search_results()
