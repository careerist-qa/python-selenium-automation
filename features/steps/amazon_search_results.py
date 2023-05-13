from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'

