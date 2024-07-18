from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


ADD_TO_CART = (By.CSS_SELECTOR, '[id*="addToCartButton"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="content-wrapper"] h4')
SIDE_NAV_ADD_TO_CART = (By.CSS_SELECTOR, '[data-test="content-wrapper"] [id*="addToCartButton"]')
AD_CONTAINER_ID = (By.ID, 'btf')


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    # sleep(6)
    context.driver.wait.until(EC.visibility_of_element_located(AD_CONTAINER_ID))   # To wait for adContainer pop up
    context.driver.refresh()    # To overcome StaleElementReferenceException by getting a new element reference
    context.driver.find_element(*ADD_TO_CART).click()
    context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME))  # To fix assert fails
    # context.driver.implicitly_wait(10)  # still assert fails by missing store_product_name dud to racing condition
    # sleep(2)    # To avoid NoSuchElementException at context.product_name in store_product_name


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART).click()


# TODO: Need to scroll to get all the products on the page.
PRODUCT_CARD_DEFAULTS = (By.CSS_SELECTOR, '[data-test="@web/ProductCard/ProductCardVariantDefault"]')
PRODUCT_CARD_RECOMMENDATION = (By.CSS_SELECTOR, '[data-test="productCardVariantRecommendation"]')
PRODUCT_DEFAULT_TITLE = (By.CSS_SELECTOR, '[data-test="product-title"]')
PRODUCT_RECOMMENDATION_TITLE = (By.CSS_SELECTOR, '[data-test="productCardVariantRecommendationTitle"]')
PRODUCT_IMAGE_P = (By.CSS_SELECTOR, '[data-test="@web/ProductCard/ProductCardImage/primary"] img')
PRODUCT_IMAGE_S = (By.CSS_SELECTOR, '[data-test="@web/ProductCard/ProductCardImage/secondary"] img')


@then('Verify all tea search results')
def verify_tea_search_results(context):
    product_card_defaults = context.driver.find_elements(*PRODUCT_CARD_DEFAULTS)
    for card_default in product_card_defaults:
        product_default_title = card_default.find_element(*PRODUCT_DEFAULT_TITLE).text + "TEST"
        product_default_image_p = card_default.find_element(*PRODUCT_IMAGE_P).get_attribute('src')
        product_default_image_s = card_default.find_element(*PRODUCT_IMAGE_S).get_attribute('src')
        print(f'Default title: {product_default_title}')
        print(f'Default primary image: \n{product_default_image_p}')
        print(f'Default secondary image: \n{product_default_image_s}')

        # For Test
        # product_default_title = ""
        # product_default_image_p = card_default.find_element(*PRODUCT_IMAGE_P).get_attribute('test')
        # product_default_image_s = card_default.find_element(*PRODUCT_IMAGE_S).get_attribute('test')

        assert product_default_title, f'Expected default title: {product_default_title} but does not exist.'
        assert product_default_image_p, f'Expected default primary image: {product_default_image_p} but does not exist.'
        assert product_default_image_s, (f'Expected default secondary image: {product_default_image_s} but does not '
                                         f'exist.')





