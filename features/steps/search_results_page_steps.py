from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then
from time import sleep

SEARCH_RESULTS_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
SIDE_NAV_PREV_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Previous']")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")


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
    TARGET_HELP_H2 = (By.XPATH, '')
    context.wait.until(
        EC.text_to_be_present_in_element(TARGET_HELP_H2,'Target Help'),
        message="'Target Help' text did not appear")
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
    context.app.search_results_page.verify_search_results_correct(expected_result)


@then('Page URL has search term {expected_part_url}')
def verify_search_results_page_url(context, expected_part_url):
    context.app.search_results_page.verify_search_results_page_url(expected_part_url)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(2)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    all_products = context.driver.find_elements(*LISTINGS)

    for product in all_products:

        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Product title not shown'
        product.find_element(*PRODUCT_IMG)
