from selenium.webdriver.common.by import By
from behave import given, when, then


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main_page()


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()


@when('Search for {item}')
def search_product(context, item):
    context.app.header.search(item)


@then('Verify header has {expected_amount} links')
def verify_header_links(context, expected_amount):
    expected_amount = int(expected_amount) # '6' => 6
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    assert len(links) == expected_amount, f'Expected {expected_amount} links but got {len(links)}'