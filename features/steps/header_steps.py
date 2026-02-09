from selenium.webdriver.common.by import By
from behave import given, when, then





@when('Search for {product}')
def search_for_product(context, product):
    context.app.header.search(product)
    #context.driver.find_element(By.ID, 'search').send_keys(product)
    #context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()


@when('Click on account button')
def click_on_account_button(context):
  context.driver.find_element(By.CSS_SELECTOR, '[aria-label="Account, sign in"]').click()


@when('Open target circle')
def open_target_circle(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()


@when('Click on Cart Icon')
def click_on_cart_icon(context):
        #context.driver.find_element(By.XPATH, '//a[@data-test="@web/CartLink"]').click()
        context.app.header.click_on_cart_icon()