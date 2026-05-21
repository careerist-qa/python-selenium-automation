from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

    @when("I click on the Sign In button")
    def step_click_signin_button(context):
       signin_button = context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']")
       signin_button.click()
       context.driver.find_element(By.CSS_SELECTOR, 'button[data-test="accountNav-signIn"]').click()
       sleep(3)

    @when("I click Sign In from the side menu")
    def step_click_signin_side_menu(context):
        side_signin = context.driver.find_element(By.CSS_SELECTOR, "button[data-test='accountNav-signIn']")
        side_signin.click()


    @then("the Sign In form should be displayed")
    def step_verify_signin_form(context):
        form = context.driver.find_element(By.CSS_SELECTOR, "input#username")
        assert form.is_displayed()