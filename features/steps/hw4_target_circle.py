from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify there are {number} benefit cells')
def verify_benefit_cells(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, '[data-test*="CellsComponent/Link"]')
    assert len(links) == number, f'Expected {number} cells but got {len(links)}'