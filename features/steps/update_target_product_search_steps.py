from selenium.webdriver.common.by import By
from behave import given, when, then


@then('Search results for product are shown')
def verify_product_results_shown(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR, 'div[data-module-type="ListingPageResultsCount"] h2').text
    assert 'results' in actual_text, f"Expected 'results' text not in {actual_text}"