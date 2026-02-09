from selenium.webdriver.common.by import By
from behave import given, when, then


   # find benefits cells
@when('Click for benefit cells')
def verify_benefits_cells(context):
     context.driver.find_element(By.XPATH, "//button[@data-test='storycard--staticButton']").click()


@then('Sign in or create account page')
def sign_in_or_create_account_page(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(),'Sign in or create account')]").text
    assert 'Sign in or create account' in actual_text, f"Expected 'Sign in or create account' text not in {actual_text}"


@when('Click for pharmacy')
def click_pharmacy(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="Pharmacy"]').click()


@then('CVS Pharmacy & Vaccines page')
def CVS_Pharmacy_Vaccines_page(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[contains(text(), 'CVS Pharmacy & Vaccines')]").text
    assert 'CVS Pharmacy & Vaccines' in actual_text, f"Expected 'CVS Pharmacy & Vaccines' text not in {actual_text}"


@when('Click for target help')
def verify_help(context):
    context.driver.find_element(By.CSS_SELECTOR, '[aria-label="Target Help"]').click()


@then('Verify the help page opens')
def verify_help_page_opens(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, "[aria-current='page']").text
    assert 'Help' in actual_text, f"Expected 'Help' text not in {actual_text}"