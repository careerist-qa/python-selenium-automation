from selenium.webdriver.common.by import By
from behave import given, when, then


COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='CellVariationHeaderWrapper']")

@given('Open target product A-88345426 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/A-88345426')


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Brown', 'Oatmeal', 'Gray', 'Black']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    for color in colors:
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text.split('\n')[1]
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'