from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(5)


CLICK_CATEGORIES = By.CSS_SELECTOR, "[aria-label='Categories']"
CLICK_CHRISTMAS = By.CSS_SELECTOR, "[data-url='/c/christmas/-/N-5xt30']"
CLICK_DEALS = By.CSS_SELECTOR,"[data-url='/c/christmas-deals/-/N-4rr05']"
CLICK_TREES = By.CSS_SELECTOR,"[src='https://target.scene7.com/is/image/Target/GUEST_5ea06363-e13a-4069-8469-cd7cbf892955?wid=315&hei=315&qlt=60&fmt=webp']"
FIRST_TREE = By.CSS_SELECTOR,"[data-test='@web/ProductCard/body']"
ADD_TO_CART = By.CSS_SELECTOR,"[aria-label*='Artificial Christmas Tree Holiday Decor with 450']"
VIEW_CART = By.CSS_SELECTOR,"[href='/cart']"




@when('Click on Categories')
def click_categories(context):
    context.driver.wait.until(EC.element_to_be_clickable(CLICK_CATEGORIES)).click()


@when('Click on Christmas button')
def click_christmas(context):
    context.driver.find_element(*CLICK_CHRISTMAS).click()



@when('Click on Christmas Deals')
def click_christmas_deals(context):
    context.driver.find_element(*CLICK_DEALS).click()



@when('Click on Christmas Trees')
def click_christmas_trees(context):
    context.driver.find_element(*CLICK_TREES).click()



@when('Click on first christmas tree')
def click_first_tree(context):
    context.driver.find_element(*FIRST_TREE).click()



@when('Click on Add to cart')
def click_add_to_cart(context):
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()


@when('Click on view cart and checkout button')
def view_cart(context):
    context.driver.find_element(*VIEW_CART).click()


@then('Verify if result is shown')
def verify_result(context):
    expected_value = "$234.99 subtotal 1 item"
    actual_result= context.driver.find_element(By.CSS_SELECTOR,"#cart-summary-heading").click()
    assert expected_value == actual_result,f'{expected_value} != {actual_result}'
    print(actual_result)




