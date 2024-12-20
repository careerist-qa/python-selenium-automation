from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Categories')
def click_categories(context):
    context.driver.find_element(By.CSS_SELECTOR, "[aria-label='Categories']").click()
    sleep(2)


@when('Click on Christmas button')
def click_christmas(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-url='/c/christmas/-/N-5xt30']").click()
    sleep(2)


@when('Click on Christmas Deals')
def click_christmas_deals(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-url='/c/christmas-deals/-/N-4rr05']").click()
    sleep(2)


@when('Click on Christmas Trees')
def click_christmas_trees(context):
    context.driver.find_element(By.CSS_SELECTOR,"[src='https://target.scene7.com/is/image/Target/GUEST_5ea06363-e13a-4069-8469-cd7cbf892955?wid=315&hei=315&qlt=60&fmt=webp']").click()
    sleep(5)


@when('Click on first christmas tree')
def click_first_tree(context):
    context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/ProductCard/body']").click()
    sleep(5)


@when('Click on Add to cart')
def click_add_to_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[aria-label*='Artificial Christmas Tree Holiday Decor with 450']").click()
    sleep(5)


@when('Click on view cart and checkout button')
def view_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,"[href='/cart']").click()
    sleep(3)


@then('Verify if result is shown')
def verify_result(context):
    expected_value = "$234.99 subtotal 1 item"
    actual_result= context.driver.find_element(By.CSS_SELECTOR,"#cart-summary-heading").click()
    assert expected_value == actual_result,f'{expected_value} != {actual_result}'
    print(actual_result)




