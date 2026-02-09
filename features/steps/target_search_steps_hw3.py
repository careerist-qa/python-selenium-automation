
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

CART_ICON = (By.CSS_SELECTOR, 'a[data-test="@web/CartLink"]')
SIGN_IN_ICON = (By.CSS_SELECTOR, 'a[id="account-sign-in"]')


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')
    sleep(2)


@when('Search for {search_text}')
def search_product(context, search_text):
    # find search field and enter text
    context.driver.find_element(By.ID, 'search').send_keys(search_text)
    # click search
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    # wait for the page with search results to load
    sleep(6)


@then('Verify correct search results shown')
def verify_search_results(context):
    expected_text = 'car'
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_text in actual_text, f'Expected {expected_text} ot in actual {actual_text}'


@when('Click on Cart icon')
def click_cart(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(5)


@then('Verify Empty cart message is shown')
def verify_empty_cart(context):
    expected_result = 'Your cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result == actual_result, f'Expected {expected_result} did not match actual {actual_result}'
    sleep(5)


@when('Click Sign in')
def click_sign_in(context):
    context.driver.find_element(*SIGN_IN_ICON).click()
    sleep(2)


@then('Verify Sign in Form opens')
def verify_sign_in(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(3)
    expected = 'Sign in or create account'
    actual = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
    assert expected == actual, f'Expected {expected} did not match actual {actual}'
    sleep(5)
