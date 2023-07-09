from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTN = (By.ID, 'nav-search-submit-button')
FOOTER_LINKS = (By.CSS_SELECTOR, ".navFooterMoreOnAmazon a")
POPUP_SIGNIN_BTN = (By.CSS_SELECTOR, "#nav-signin-tooltip .nav-action-signin-button")


@given('Open amazon main page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click on button from SignIn popup')
def click_sign_in_popup_btn(context):
    context.driver.wait.until(
        EC.element_to_be_clickable(POPUP_SIGNIN_BTN),
        message='Signin btn not clickable'
    ).click()


@when('Search for {search_word}')
def search_amazon(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    actual_result = context.driver.find_element(*RESULT_TEXT).text
    assert expected_result == actual_result, f'Error! Expected {expected_result} bot got actual {actual_result}'


@then("Verify there are {expected_amount} links")
def verify_link_count(context, expected_amount):
    links_count = len(context.driver.find_elements(*FOOTER_LINKS)) # 36
    expected_amount = int(expected_amount)
    assert links_count == expected_amount, f"Expected {expected_amount} links, but got {links_count}"


