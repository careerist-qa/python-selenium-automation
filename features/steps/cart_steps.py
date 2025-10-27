from behave import when,given,then
from selenium import webdriver
from selenium.webdriver.common.by import By


from time import sleep


@given('Open Target page')
def open_main(context):
     context.driver.get("https://www.target.com/")


@when('Click on add to cart icon')
def click_add_to_cart(context):
     context.driver.find_element(By.CSS_SELECTOR,"#headerPrimary > a.styles_ndsLink__GUaai.styles_onLight__QKcK7.sc-7f25f5f4-1.sc-5c0d75eb-0.jaPeIi.iQmnSG > div > svg").click()

@then('verify empty cart message')
def verify_empty_cart_message(context):
    expected_text= "Your cart is empty"
    actual_text= context.driver.find_element(By.XPATH,"//h1[contains(@class,'M5gHh')]").text
    assert actual_text== expected_text, f"Expected:{expected_text} but got Actual:{actual_text}"








