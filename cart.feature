from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Verify correct search results show')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='lp-resultsCount']").text
    expected_text = 'tea'
    assert expected_text in actual_text, f'Error. Text {expected_text} not in {actual_text}'

