from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("I open Target homepage")
def step_open_homepage(context):
    context.driver.get("https://www.target.com")

@when("I search for a product")
def step_search_product(context):
    search_term = context.config.userdata.get("product", "laptop")
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(search_term)
    search_box.submit()

@then("I should see search results related to the product")
def step_verify_results(context):
    product = context.config.userdata.get("product", "laptop")
    results = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='product-title']")
    assert any(product.lower() in r.text.lower() for r in results)

@given("I open the Target Circle page")
def step_open_circle(context):
    context.driver.get("https://www.target.com/circle")

@then("I should see 2 storycards under Unlock added value")
def step_verify_storycards(context):
    cards = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='story-card']")
    assert len(cards) == 2, f"Expected 2 storycards, found {len(cards)}"


@when("I add the first product to the cart")
def step_add_first_product(context):
    first_product = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='product-title']")[0]
    first_product.click()

    add_btn = context.driver.find_element(By.CSS_SELECTOR, "[data-test='addToCartButton']")
    add_btn.click()

    time.sleep(2)  # wait for modal

@then("the product should appear in the cart")
def step_verify_cart(context):
    context.driver.get("https://www.target.com/cart")

    cart_items = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='cart-item']")
    assert len(cart_items) > 0, "Cart is empty!"