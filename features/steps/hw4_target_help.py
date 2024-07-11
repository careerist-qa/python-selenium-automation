from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify {number_elements} UI elements are present of the page')
def verify(context, number_elements):
    # Locate Target Help
    container_1 = context.driver.find_elements(By.CSS_SELECTOR, 'html body form section div div div h2')
    # Locate search help, icon
    container_2 = context.driver.find_elements(By.CSS_SELECTOR, 'html body form section div div div input')
    # Locate track an order, contact us
    container_3 = context.driver.find_elements(By.CSS_SELECTOR, 'html body form section div div.col-lg-12')
    # Locate Browse all Help pages
    container_4 = context.driver.find_elements(By.CSS_SELECTOR, 'html body div div div div span form h2')

    total_elements = len(container_1) + len(container_2) + len(container_3[1:]) + len(container_4)
    assert total_elements == int(number_elements), f'Expected {number_elements} UI elements, but got {total_elements}'
