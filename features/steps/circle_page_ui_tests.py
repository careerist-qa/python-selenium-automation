from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify circle page has {expected_amount} benefit cells')
def verify_circle_page_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/slingshot-components/CellsComponent/Link']")
    assert len(cells) == expected_amount, f'Expected int{expected_amount} cells but got {len(cells)}'