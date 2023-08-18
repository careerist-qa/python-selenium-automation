from behave import given, when, then
from selenium.webdriver.common.by import By



@when('Search for table')
def search_on_amazon(context):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('table')
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()


@then('Verify search result is correct')
def verify_search_result(context):
    expected_result = '"table"'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, '.a-color-state.a-text-bold').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'