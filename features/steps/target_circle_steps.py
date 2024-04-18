from selenium.webdriver.common.by import By
from behave import given, then
from time import sleep

VERIFY_CELLS_SHOWN = (By.CSS_SELECTOR, "[data-component-title*='BaseDrivers'] div.cell-item-content")


@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify there are cells shown')
def verify_cells_shown(context):
    cells = context.driver.find_elements(*VERIFY_CELLS_SHOWN)
    assert len(cells) > 0, "No cells are shown on the page"
    sleep(6)
