from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDE_NAV_PREV_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Previous']")


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()


@when('Click on Add to Cart button for product {i}')
def click_add_to_cart_by_index(context, i):
    # Find all Add to cart buttons, click on a button by index:
    # product 1 -> index 0
    # product 2 -> index 1, etc.
    context.driver.find_elements(*ADD_TO_CART_BTN)[int(i)-1].click()


@when('Store product name')
def store_product_name(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Side nav did not open')
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('Store product name to a list')
def store_product_names(context):
    context.wait.until(EC.presence_of_element_located(SIDE_NAV_PRODUCT_NAME), message='Side nav did not open')
    current_product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    try:  # try to add a product to context.product_names:
        context.product_names.append(current_product_name)
    except AttributeError:  # if context.product_names not set, set it and put the current_product_name itno it:
        context.product_names = [current_product_name]


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(2)


@when('Close side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_PREV_BUTTON).click()


@then('Search results for {expected_result} are shown')
def verify_search_results_correct(context, expected_result):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_HEADER).text
    assert expected_result in actual_text, f'Expected word {expected_result} not in {actual_text}'


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    url = context.driver.current_url
    assert expected_part_url in url, f'Expected {expected_part_url} not in {url}'

