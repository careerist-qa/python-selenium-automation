from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

RESULT_TEXT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_TITLE = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMG = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


@then('Verify search results shown for {expected_result}')
def verify_search_results(context, expected_result):
    context.app.search_results_page.verify_search_results(expected_result)


@when('Click on the first product')
def click_first_product(context):
    context.driver.find_element(*PRODUCT_PRICE).click()
    sleep(2)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)
    print(all_products) # => [WebEl1, WebEl2, WebEl3, ..., WebEl60]

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        print(title)
        assert title, 'Title should not be blank'
        assert product.find_element(*PRODUCT_IMG).is_displayed(), 'Image is not found'
