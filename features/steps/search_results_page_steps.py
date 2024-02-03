from selenium.webdriver.common.by import By
from behave import given, when, then

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    url = context.driver.current_url
    assert expected_part_url in url, f'Expected {expected_part_url} not in {url}'

