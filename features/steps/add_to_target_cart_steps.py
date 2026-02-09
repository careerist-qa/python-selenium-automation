from time import sleep

from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium. webdriver.support import expected_conditions as EC

@when('Click on add to cart button')
def click_add_to_cart(context):
    sleep(20)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='chooseOptionsButton']").click()
    sleep(5)
    context.driver.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Fulfillment"] [id*="addToCartButtonOrTextIdFor"]'))).click()


@then('Confirm added to cart message from side navigation')
def added_to_cart_message_from_side_navigation(context):
    sleep(5)
    actual_text = context.driver.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h2[data-test="modal-drawer-heading"] span[class="h-text-lg"]'))).text

    expected_text = 'Added to cart'
    assert actual_text==expected_text, f'Expected text to be {expected_text}, but got {actual_text}'
