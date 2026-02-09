from selenium.webdriver.common.by import By
from behave import given, when, then





@then('Search results for cart button')
def search_results_for_cart(context):
    context.app.search_results_page.verify_search_results()







