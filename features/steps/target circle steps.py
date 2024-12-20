from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Target Circle button')
def search_circle(context):
    context.driver.find_element(By.CSS_SELECTOR,"#utilityNav-circle").click()
sleep(5)


@then('Verify at least 10 cells present')
def results_for_circle(context):
    actual_results_circle = context.driver.find_elements(By.CSS_SELECTOR, "[data-test='@web/slingshot-components/CellsComponent/Link']")
    print(actual_results_circle)

    assert len(actual_results_circle) >= 10,f'Expected 10 links, but got {len(actual_results_circle)}'
    sleep(3)