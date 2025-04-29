from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



LISTINGS = (By.CSS_SELECTOR, "[data-test*='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')

@given('Open Target product page')
def open_product_page(context):
    context.driver.get('https://www.target.com/c/laundry-care-household-essentials/all-deals/-/N-5xsyrZakkos')
    sleep(4)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    # To see ALL listings (comment out if you only check top ones):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")

    # Find all products:
    all_products = context.driver.find_elements(*LISTINGS)
    # print(all_products)
    assert len(all_products) > 0, 'No products found'

    for product in all_products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(title)
        product.find_element(*PRODUCT_IMG)
