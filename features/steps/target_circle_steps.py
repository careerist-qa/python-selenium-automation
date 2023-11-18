from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open test case page')
def webpage_url(context):
    context.driver.get('https://www.target.com/')
    sleep(6)


@when('Click on Target Circle')
def target_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test*='TargetCircle']").click()
    sleep(6)


#Hola Teach, I was hung up on verification for @then. What I was attempting to do is count the number of links I found for my locator.
#and then compare it to the number in the steps for the feature. I often get confused as to, what tool(method) to use out of my toolbelt(what Ive learned)
#to apply. I kind-of mapped what envisioned, just need a little guidance.
@then('Verify {number} benefits boxes')
def verify_links(context):
    number_of_links = int('number')
    expected_number_links = context.driver.find_elements(By.CSS_SELECTOR, "li.styles__BenefitCard-sc-9mx6dj-2.lgQxFm")
    number_of_links == expected_number_links, f''
    context.driver.quit()
