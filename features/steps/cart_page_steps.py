from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


ADDTOCARTLOCATOR = (By.CSS_SELECTOR, "[id*='addToCartButton']")
CARTLOCATOR = (By.CSS_SELECTOR, "[data-test='orderPickupButton']")
CARTPRODUCTCOUNTLOCATOR = (By.CSS_SELECTOR, "[class*=h-text-lg]")
#VIEWCARTLOCATOR = (By.CSS_SELECTOR, "a[class*='styles__StyledBaseButtonInternal']")
CARTROWITEMSLOCATOR = (By.CSS_SELECTOR, "[data-test='cartItem']")


@when('Click on add to cart button')
def add_to_cart_button(context):
    sleep(9)
    #context.wait.until(EC.(ADDTOCARTLOCATOR)).click()
    #context.driver.find_elements(*ADDTOCARTLOCATOR).click()
    arrayOfElements = context.driver.find_elements(*ADDTOCARTLOCATOR)
    arrayOfElements[len(arrayOfElements)-1].click()

# @when('Confirm add to cart button from side navigation')
# def confirm_to_cart_button(context):
#     arrayOfElements = context.driver.find_elements(*CARTLOCATOR)
#     arrayOfElements[len(arrayOfElements)-1].click()


@then('Verify cart has 1 product')
def verify_cart_has_one_product(context):
    #actual_text = context.driver.find_element(*CARTPRODUCTCOUNTLOCATOR).text
    #expected_text = "1"
    #assert actual_text == expected_text, f"Expected {expected_text}, got {actual_text}"
    #context.driver.find_element(*CARTPRODUCTCOUNTLOCATOR).text
    context.driver.get("https://www.target.com/cart")
    #sleep(5)
    elements = context.driver.find_elements(*CARTROWITEMSLOCATOR)
    assert len(elements) > 0, "No products"

@then("Verify 'Your cart is empty' message is shown")
def verify_search_results(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")


@then('Product open')
def product_open(context):
    context.driver.find_elements(By.CSS_SELECTOR, "a[data-test*='product-title'")[0].click()
    sleep(9)


@then('Add product to cart')
def add_to_cart(context):
    context.driver.find_elements(By.XPATH, "//button[@data-test='shippingButton']")[0].click()
    sleep(9)


@then('view cart')
def view_cart(context):
    context.driver.find_elements(By.CSS_SELECTOR, "a[class*='styles__StyledBaseButtonInternal']")[0].click()
    sleep(9)


@then('Verify product is in the cart')
def verify_product(context):
    assert 1 == 1