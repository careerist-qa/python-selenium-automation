from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify {product} search result is shown')
def verify_search_result(context, product):
    result_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert product in result_text, f'Expected {product} is not in actual {result_text}'


@then('Verify correct search URL opens for {product}')
def verify_search_url(context, product):
    search_url = context.driver.current_url
    assert product in search_url, f'Expected {product} is not in actual {search_url}'


list_add_products = []


@when('Add the first product to cart')
def add_first_product_to_cart(context):
    #sleep(10)
    product_titles = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="product-title"]')
    options_buttons = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="chooseOptionsButton"]')
    i = 0
    for options_button in options_buttons:
        if options_button.text != 'Add to cart':
            i += 1
            continue
        else:
            list_add_products.append(product_titles[i].text[:20])
            options_button.click()
            sleep(2)
            break


list_add_prices = []


@when('Click "Add to cart" button')
def click_add_to_cart(context):
    sleep(2)
    product_prices = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="product-price"]')
    list_add_prices.append(float(product_prices[-1].text[1:]))
    add_to_cart_button = context.driver.find_elements(By.CSS_SELECTOR, '[id*="addTo"]')[-1]
    add_to_cart_button.click()
    sleep(2)


@when('Click "View cart & check out" button')
def click_view_cart(context):
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR, 'a[href="/cart"]').click()
    sleep(2)


@when('Click "Continue shopping" button')
def click_continue_shopping(context):
    sleep(2)
    context.driver.find_element(By.XPATH, '//button[text()="Continue shopping"]').click()
    sleep(2)



