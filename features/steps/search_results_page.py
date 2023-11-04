from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Verify search worked for {product}')
def verify_search(context, product):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert product in search_results_header, f'Expected text {product} not in {search_results_header}'


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    assert expected_keyword in context.driver.current_url, \
        f'Expected {expected_keyword} not in {context.driver.current_url}'
