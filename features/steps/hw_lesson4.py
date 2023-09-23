from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from behave import given, then



@then("Click on Best Sellers Page")
def best_sellers_page(context):
    context.driver.find_element(By.XPATH, "//a[@href='/gp/bestsellers/?ref_=nav_cs_bestsellers']").click()

@then("Verify there are 5 links")
def verify_links(context):
    context.driver.find_elements(By.CSS_SELECTOR, "#zg_header a")


# wait 10 seconds
sleep(10)
