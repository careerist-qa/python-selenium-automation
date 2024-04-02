from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target.com')
def open_target(context):
    context.driver.get("https://www.target.com/")
    sleep(2)


@when('Click Sign In button')
def click_sign_in_button(context):
    sign_in_button = context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    sign_in_button.click()
    sleep(2)


@when('Click on the Sign In link from the right side navigation menu')
def click_sign_in_link(context):
    sign_in_link = context.driver.find_element(By.CSS_SELECTOR, ".styles__ListItemText-sc-diphzn-1")
    sign_in_link.click()
    sleep(2)


@then('Verify Sign In form opened')
def verify_sign_in_form_opened(context):
    sign_in_form = context.driver.find_element(By.CSS_SELECTOR, ".styles__StyledHeading-sc-1xmf98v-0")
    assert sign_in_form.is_displayed(), "Sign In form is not displayed"