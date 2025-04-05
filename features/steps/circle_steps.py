from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open the Target Circle page')
def open_target_circle_page(context):
    context.driver.get("https://www.target.com/circle")


@then('Verify there are at least 10 benefit cells')
def verify_benefit_cells(context):
    benefits = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".cell-item-content"))
    )
    assert len(benefits) >= 10, f"Expected at least 10 benefit cells, got {len(benefits)}"


@given('Open the Target homepage')
def open_target_homepage(context):
    # Replace with the actual URL of Target's homepage
    context.driver.get("https://www.target.com")
    # Verify homepage has loaded by checking the title
    assert "Target" in context.driver.title, "Target homepage did not load properly."


@when('Search for a product "{product_name}"')
def search_for_product(context, product_name):
    # Find the search input field
    search_box = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input#search"))
    )

    # Enter the product name and press ENTER
    search_box.send_keys(product_name + Keys.RETURN)


@when('Add the first product to the cart')
def add_first_product_to_cart(context):
    # Wait for the search results to load and select the first product
    first_product = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div[data-test='product-card']"))
    )
    first_product.click()

    # Wait for the "Add to Cart" button to be clickable
    add_to_cart_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-test='addToCartButton']"))
    )
    add_to_cart_button.click()


@then('Verify the product is in the cart')
def verify_product_in_cart(context):
    # Open the cart page
    cart_icon = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test='cart']"))
    )
    cart_icon.click()

    # Check if the cart contains at least one cart item
    cart_items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div[data-test='cart-item']"))
    )

    # Assert there is at least one item in the cart
    assert len(cart_items) > 0, "No items were found in the cart!"
    print(f"Cart contains {len(cart_items)} item(s).")
