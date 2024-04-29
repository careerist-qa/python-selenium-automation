from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support.wait import WebDriverWait
import json


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)


@then('Verify user can click through shoes colors')
def click_and_verify_colors(context):
    expected_colors = ['dark khaki', 'black/gum', 'stone/grey', 'white/gum']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
   # colors = context.driver.wait.until((By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")).click()
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click through jeans colors')
def click_and_verify_colors(context):
    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)  # [webelement1, webelement2, webelement3]
    #colors = context.driver.wait.until(EC.element_to_be_clickable(COLOR_OPTIONS).click())
    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'