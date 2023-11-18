from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open targets home page')
def targets_url(context):
    context.driver.get('https://www.target.com/')
    sleep(6)


@when('Type {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(By.CSS_SELECTOR, '#search')
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click new search button')
def click_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='SearchButton']").click()
    sleep(6)


@when('Add to cart')
def add_product_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, '#addToCartButtonOrTextIdFor15013944').click()
    sleep(6)


@then('Verify {search_word} is added in cart')
def verify_item_in_cart(context, search_word):
    search_results_cart = context.driver.find_element(By.CSS_SELECTOR, "h4[class='styles__StyledHeading-sc-1xmf98v-0 dQsNJZ']").text
    assert search_word in search_results_cart, f'Expected text {search_word} not in {search_results_cart}'
    sleep(6)
    context.driver.quit()
