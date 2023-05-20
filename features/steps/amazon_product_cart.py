from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
#$$("a[href*='/Womens-Plus-SizeStretch-Jersey-Length-Leggings/dp/B01B3ITZS'][href*='keywords=activewear']")


SEARCH_PRODUCT_FIELD = (By.CSS_SELECTOR, 'input#twotabsearchtextbox')
SEARCH_ICON_BUTTON = (By.CSS_SELECTOR, 'input#nav-search-submit-button')
#PRODUCT_IMAGE = (By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/I/614BIw8TszL._AC_UL400_.jpg']")
#PRODUCT_IMAGE = (By.CSS_SELECTOR, "img[src='https://m.media-amazon.com/images/I/614BIw8TszL._AC_UL400_.jpg']")
#PRODUCT_IMAGE = (By.CSS_SELECTOR, 'img[src="https://m.media-amazon.com/images/I/614BIw8TszL._AC_UL400_.jpg"][data-image-index="2"]')
#PRODUCT_IMAGE = (By.CSS_SELECTOR, "img[data-image-index='2'][alt*='Just My Size']")
#PRODUCT_IMAGE = (By.CSS_SELECTOR,"span#productTitle")
ALL_PRODUCTS = (By.XPATH, "//div[@data-component-type='s-search-result']//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
#PRODUCT_IMAGE = (By.XPATH, "//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']")
ADD_TO_CART = (By.CSS_SELECTOR,'input#add-to-cart-button')
PRODUCT_IN_CART = (By.CSS_SELECTOR, "span#nav-cart-count")
PRODUCT_SIZE = (By.CSS_SELECTOR, "input[aria-labelledby='size_name_1-announce']")

@given('Enter Amazon page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')

@when('Enter  product {search_word} in search field')
def search_product(context,search_word):
    search_field=context.driver.find_element(*SEARCH_PRODUCT_FIELD)
    search_field.clear()
    search_field.send_keys(search_word)
    sleep(4)

@when('Click the search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_ICON_BUTTON).click()
    sleep(4)

@then('choose your product from result page')
def choose_product_result(context):
    all_products = context.driver.find_elements(*ALL_PRODUCTS)
    all_products[0].click()
    sleep(5)



@then('click add to cart button')

def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(4)

@then('confirm that selected product in the cart')

def confirm_select_product_cart(context):
    context.driver.find_element(*PRODUCT_IN_CART).click()
    sleep(4)

