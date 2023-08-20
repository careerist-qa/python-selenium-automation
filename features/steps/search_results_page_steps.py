from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')


@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
    actual_result = context.driver.find_element(*SEARCH_RESULT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

