
from behave import given,when,then
from selenium.webdriver.common.by import By


@given('Open the Target page')
def open_main(context):
    context.driver.get("https://www.target.com/")

@when('Click signin button')
def click_signin_button(context):
    context.driver.find_element(By.XPATH,"//span[contains(.,'Account')]").click()
    context.driver.find_element(By.XPATH,"//button[@data-test='accountNav-signIn']").click()

@then('Verify signin form opened')
def verify_signin_form_opened(context):
    actual_text= context.driver.find_element(By.XPATH,"//h1[contains(.,'Sign in or create account')]").text
    expected_text= 'Sign in or create account'
    assert actual_text in expected_text, f'Expected:{expected_text} but got Actual:{actual_text}'




