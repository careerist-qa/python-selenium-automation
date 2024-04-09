from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('open target main page')
def open_target(context):
    context.driver.get("https://www.target.com/")


@when("Search for 'coffee'")
def search_for_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('coffee')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(6)


@then('Verify search results are shown')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'coffee' in actual_text, f'Error! coffee not found in {actual_text}'


@when('Click on cart icon')
def click_on_cart_icon(context):
    context.driver.find_element(By.XPATH, "//div[@data-test='@web/CartIcon']").click()


@then("Verify 'Your cart is empty' message is shown")
def verify_search_results(context):
    context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']")



#click signin
@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()
    sleep(6)


#click signin from side bar
#driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
#sleep(6)
@when('Click on sign in from right side navigation menu')
def click_on_sign_in(context):
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
    sleep(6)


@then('Verify Sign In form opened')
def verify_sign_in(context):
    actual_text=context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    print(actual_text)