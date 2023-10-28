from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for coffee')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(6)  # wait for ads to disappear


@then('Verify search worked')
def verify_search(context):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert 'coffee' in search_results_header, f'Expected text coffee not in {search_results_header}'


@then('Verify search result url')
def verify_search_url(context):
    assert 'coffee' in context.driver.current_url
