from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given("I open Target homepage")
def step_open_homepage(context):
    context.driver.get("https://www.target.com")