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
    context.driver.find_element(By.CSS_SELECTOR, "._p13n-zg-nav-tab-all_style_zg-tabs-li-selected-div__3tHnP")
    context.driver.find_element(By.XPATH, "//a[@href='/gp/new-releases/ref=zg_bs_tab_bsnr']")
    context.driver.find_element(By.XPATH, "//a[@href='/gp/movers-and-shakers/ref=zg_bs_tab_bsms']")
    context.driver.find_element(By.XPATH, "//a[@href='/gp/most-wished-for/ref=zg_bs_tab_mw']")
    context.driver.find_element(By.XPATH, "//a[@href='/gp/most-gifted/ref=zg_bs_tab_mg']")

# wait 10 seconds
sleep(10)
