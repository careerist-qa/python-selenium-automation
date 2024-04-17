from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, "search")
SEARCH_BUTTON = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.XPATH, "//div[@data-test='@web/CartIcon']")
HEADER =(By.CSS_SELECTOR, "[class*='styles__UtilityHeaderWrapper']")
HEADER_LINKS = (By.CSS_SELECTOR, "a[id*='utilityNav']")


@given('Open target main page')
def open_target(context):
    context.driver.get("https://www.target.com/")


@when("Search for '{item}'")
def search_for_product(context, item):
    context.driver.find_element(*SEARCH_INPUT).send_keys(item)
    context.driver.find_element(*SEARCH_BUTTON).click()
    sleep(9)


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()


@then('Verify header in shown')
def verify_header_shown(context):
    context.driver.find_element(*HEADER)

@then('Verify header has 5 links')
def verify_header_links(context):
    links = context.driver.find_elements(*HEADER_LINKS)
    print(links)
    assert len(links) == 6, f'Expected 6 links but got {len(links)}'


