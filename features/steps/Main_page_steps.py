from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescText')

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://amazon.com')
    sleep(2)
    context.driver.refresh()

@when('Click Orders')
def click_orders(context):
    context.driver.find_element(By.XPATH, "//span[contains(text(), '& Orders')]").click()


@when('Search for {search_word}')
def search_on_amazon(context, search_word):
    context.driver.find_element(By.ID, 'twotabsearchtextbox').send_keys(search_word)
    context.driver.find_element(By.ID, 'nav-search-submit-button').click()

@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    print(links)
    print(f'Total links:{len(links)}')
    assert len(links) == expected_amount,f'Expected {expected_amount} links but got {len(links)}'


