from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Sign In icon')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(2)


@when('Click on Sign In from right side menu')
def click_sign_in_right(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    sleep(2)


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, "form[method='post']")
