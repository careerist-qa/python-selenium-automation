from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@when('Click on Target Circle button')
def search_circle(context):
    context.driver.wait.until(EC.element_to_be_clickable(*SEARCH_CIRCLE)).click()


@then('Verify at least 10 cells present')
def results_for_circle(context):
    actual_results_circle = context.driver.find_elements(*RESULTS)
    print(actual_results_circle)

    assert len(actual_results_circle) >= 10,f'Expected 10 links, but got {len(actual_results_circle)}'
    sleep(3)