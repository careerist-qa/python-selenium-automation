from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep



@when('Click on dog image')
def click_dog_img(context):
    context.app.not_found_page.click_dog_img()


@when('Switch to new window')
def switch_window(context):
    context.app.not_found_page.switch_to_new_window()

