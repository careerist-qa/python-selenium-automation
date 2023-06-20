
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLLECTION_OF_PRODUCT_COLORS=(By.CSS_SELECTOR,"#variation_color_name li")

SELECTED_PRODUCT            =(By.CSS_SELECTOR,"#variation_color_name .selection")
@given( 'Open Amazon product page')
def open_google(context):
    context.driver.get('https://www.amazon.com/gp/product/B07BJKRR25/')



@then('Verify that users can click each product')
def click_each_product(context):
    # collection of all the pant product in product_list
    product_list=context.driver.find_elements(*COLLECTION_OF_PRODUCT_COLORS)

    #for loop for iterating product list elements(each product)
    for product in product_list:
        product.click()
        # selected product color will be print when we use .text comment
        product_color = context.driver.find_element(*SELECTED_PRODUCT).text
        print(product_color)

