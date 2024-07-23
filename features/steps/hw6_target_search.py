from behave import given, when, then
from time import sleep


@then('Verify coffee search results by Page')
def verify_coffee_in_results(context):
    context.hw6app.hw6_search_page.verify_text()
    context.hw6app.hw6_search_page.verify_url()
    sleep(2)
