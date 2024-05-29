from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC

product_info = (By.CSS_SELECTOR, 'a[data-test="product-title"]')
bestsellers = (By.CSS_SELECTOR, '#zg_header a')
banner = (By.CSS_SELECTOR, 'span#zg_banner_text')


@then('Verify product names and images displays')
def verify_product(context):
    context.driver.wait.until(EC.presence_of_all_elements_located(product_info))


@when('Click headers')
def click_headers(context):
    sleep(10)
    top_links = context.driver.find_elements(*bestsellers)
    print(top_links)

    for i in range(len(top_links)):  # for x from 0 to 4
        link_to_click = context.driver.find_elements(*bestsellers)[i]
        link_text = link_to_click.text
        link_to_click.click()
        header_text = context.driver.find_element(*banner).text
        assert link_text in header_text, f'Expected {link_text} to be in {header_text}'




