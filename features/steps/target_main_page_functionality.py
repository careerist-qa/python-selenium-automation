from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/CartIcon"]').click()


@then("'Your cart is empty' message is shown")
def verify_message(context):
    expected = 'Your cart is empty'
    actual = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/AccountLink"]').click()


@when('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="accountNav-signIn"]').click()


@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    expected = 'Sign into your Target account'
    actual = context.driver.find_element(By.CSS_SELECTOR, 'h1[class*="AuthHeading"]').text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'


@when('Search for {product_text}')
def search_product(context, product_text):
    context.driver.find_element(By.ID, 'search').send_keys(product_text)
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()


@then('Verify search worked for {search_result}')
def verify_search(context, search_result):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, '[data-test="resultsHeading"]').text
    assert search_result in search_results_header, f'Expected text {search_result} not in {search_results_header}'


@then('Verify {expected_text} in search result url')
def verify_search_url(context, expected_text):
    assert expected_text in context.driver.current_url, \
        f'Expected {expected_text} not in {context.driver.current_url}'