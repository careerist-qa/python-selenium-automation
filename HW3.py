from selenium.context.driver.chromium.context.driver import ChromiumDriver

#Join Stack Overflow
Link Text:Join Stack Overflow
driver.find_element(By.LINK_TEXT, "Join Stack Overflow").send_keys("")

#"Sign up”, you agree to our"
id="By clicking “Sign up”, you agree to our"
driver.find_element(By.ID,"Sign up, you agree to our")

#and acknowledge you have read our
id="and acknowledge you have read our"
driver.find_element(By.ID,"and acknowledge you have read our")

#terms of service
Link Text: terms of service
driver.find_element(By.LINK_TEXT, "terms of service").send_keys("")

#privacy policy
Link Text: privacy policy
driver.find_element(By.LINK_TEXT, "privacy policy").send_keys("")

#signup-google
id="signup-google"
driver.find_element(By.ID,"signup-google")

#signup-github
id="signup-github"
driver.find_element(By.ID,"signup-github")

#signup-modal-submit-button
id="signup-modal-submit-button"
driver.find_element(By.ID,"signup-modal-submit-button")

#svg-icon iconEyeOff
id="svg-icon iconEyeOff"
driver.find_element(By.ID,"svg-icon iconEyeOff")

#signup-modal-email
id="signup-modal-email"
driver.find_element(By.ID,"signup-modal-email")

#signup-modal-password
id="signup-modal-password"
driver.find_element(By.ID,"signup-modal-password")

from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


Feature: Target Cart
  As a user
  I want to view my cart
  So that I can see if it is empty

  Scenario: Verify empty cart message
    Given I open Target homepage
    When I click on the cart icon
    Then I should see "Your cart is empty"


from behave import given, when, then
from selenium.webdriver.common.by import By

@given("I open Target homepage")
def step_open_homepage(context):
    context.driver.get("https://www.target.com")

@when("I click on the cart icon")
def step_click_cart(context):
    cart_icon = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']")
    cart_icon.click()

@then('I should see "Your cart is empty"')
def step_verify_empty_cart(context):
    message = context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMessage']")
    assert "Your cart is empty" in message.text

Feature: Sign In Navigation
  As a logged out user
  I want to navigate to the Sign In page
  So that I can log into my account

  Scenario: Navigate to Sign In from homepage
    Given I open Target homepage
    When I click on the Sign In button
    And I click Sign In from the side menu
    Then the Sign In form should be displayed

from behave import given, when, then
from selenium.webdriver.common.by import By

@when("I click on the Sign In button")
def step_click_signin_button(context):
    signin_button = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
    signin_button.click()

@when("I click Sign In from the side menu")
def step_click_signin_side_menu(context):
    side_signin = context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
    side_signin.click()

@then("the Sign In form should be displayed")
def step_verify_signin_form(context):
    form = context.driver.find_element(By.CSS_SELECTOR, "input#username")
    assert form.is_displayed()

driver.quit();