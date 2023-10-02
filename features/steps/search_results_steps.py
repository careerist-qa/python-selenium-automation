from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@then('Verify search result is {expected_result}')
def verify_search_result(context,expected_result):
    context.app.search_result_page.verify_search_result(expected_result)
    # actual_result = context.driver.find_element(SEARCH_RESULT).text
    # assert expected_result == actual_result, f'Error expected {expected_result} did not match actual {actual_result}'

@then('Select Product')
def select_product(context):
    context.app.search_result_page.product_select()




