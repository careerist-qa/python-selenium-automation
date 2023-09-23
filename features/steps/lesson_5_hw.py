from behave import when, then, given
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
@given('Open Amazon Product  Page')
def open_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/dp/B0C4V5L5QK/')

@then('Verify user can click through colors')
def verfiy_click_colors(context):
    expected_colors = ['Atomic Blue', 'Aventurine', 'Black']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)


    for color in colors[:3]:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text
        print(current_color)
        actual_colors.append(current_color)

    assert actual_colors == expected_colors, f'Excepted {excepted_colors} did not match actual {actual_colors}'