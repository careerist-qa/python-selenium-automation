from selenium.webdriver.common.by import By
from behave import then
from time import sleep


SEARCH_RESULT_HEADER =(By.XPATH, "//div[@data-test='resultsHeading']")
LISTINGS =(By.CSS_SELECTOR, "[data-test='@web/ProductCard/body']")
PRODUCT_TITLE =(By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMAGE =(By.CSS_SELECTOR, "[data-test*='@web/ProductCard/ProductCar']")

@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    actual_text = context.driver.find_element(*SEARCH_RESULT_HEADER).text
    assert expected_item in actual_text, f'Error! {expected_item} not found in {actual_text}'


@then('Verify that every product has a name and an image')
def verify_product_name_image(context):

    context.driver.execute_script("window.scrollBy(0, 2000);")
    sleep(5)

    context.driver.execute_script("window.scrollBy(0, 2000);")

    all_products = context.driver.find_elements(*LISTINGS)

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product not found in listing'
        product.find_element(*PRODUCT_IMAGE)