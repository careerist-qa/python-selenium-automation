from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from hw4_target_search import *

list_cart_products = []


@then('All the products are shown on the cart')
def check_the_cart(context):
    cart_item_titles = context.driver.find_elements(By.CSS_SELECTOR, '[data-test="cartItem-title"]')
    for title in cart_item_titles:
        list_cart_products.append(title.text[:20])

    add_subtotal = sum(list_add_prices)
    cart_summary_subtotal = context.driver.find_element(By.XPATH, '//span[contains(text(), "sub")]').text
    cart_subtotal = float(cart_summary_subtotal.replace("subtotal", "").split()[0][1:])
    print(f'List Add Products: {sorted(list_add_products)}')
    print(f'List Cart Products: {sorted(list_cart_products)}')
    print(f'List Add Prices: {sorted(list_add_prices)}')
    print(f'Add Subtotal: {add_subtotal}')
    print(f'Cart Subtotal: {cart_subtotal}')
    assert "{:.2f}".format(add_subtotal) == "{:.2f}".format(cart_subtotal), f'Expected subtotal price ${add_subtotal} to be equal to cart subtotal price ${cart_subtotal}'
    assert sorted(list_add_products) == sorted(list_cart_products), f'Expected added items {list_add_products} are not equal to cart items {list_cart_products}'
    list_add_products.clear()
    list_add_prices.clear()
    list_cart_products.clear()
    sleep(2)
