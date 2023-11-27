from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


BENEFIT_BOXES = (By.CSS_SELECTOR, "li[class*='styles__BenefitCard']")
SCROLL_SCRIPT = "document.querySelector('.styles__BenefitsHeading-sc-9mx6dj-0').scrollIntoView(true);"


@given('Open Target Circle page')
def open_circle_page(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {number} benefit boxes on the Circle page')
def verify_benefit_boxes(context, number):
    context.driver.wait.until(EC.visibility_of_element_located(BENEFIT_BOXES))
    context.driver.execute_script(SCROLL_SCRIPT)
    sleep(2)

    assert len(context.driver.find_elements(*BENEFIT_BOXES)) == int(number), \
        f'Error, unexpected number of benefit boxes'
