from selenium.webdriver.common.by import By
from behave import then


SEARCH_RESULT_HEADER =(By.XPATH, "//div[@data-test='resultsHeading']")
@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert expected_item in actual_text, f'Error! {expected_item} not found in {actual_text}'
