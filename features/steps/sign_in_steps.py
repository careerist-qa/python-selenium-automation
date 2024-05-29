from selenium.webdriver.common.by import By
from behave import then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@then('Verify Sign in page opened')
def verify_sign_in_opened(context):
    wait = WebDriverWait(context.driver, 10)
    context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
    #context.driver.wait.until(EC.url_contains('ap/signin'), message='Signin URL did not open')