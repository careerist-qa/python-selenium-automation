from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


color_options = (By.CSS_SELECTOR,'ul.a-declarative.a-button-list li')
curr_color = (By.CSS_SELECTOR, 'div.a-section span.selection')


@given('Open Target product {target_item} page')
def target_product_page(context, target_item):
    context.driver.get(f'https://www.Amazon.com/dp/{target_item}')


@when('Verify color options')
def verify_color_options(context):
    context.driver.find_element(*color_options).click()

    all_color_options = context.driver.find_elements(*color_options)
    print('All colors:', all_color_options)
    expected_colors = ['Aqua Blue Poppy', 'Black', 'Black White Animal Print', 'Bright Pink', p00pp0'Dark Blue White Petal', 'French Blue', 'Navy', 'Red Leafy Floral']

    actual_colors = []
    for color in all_color_options[:8]:
        color.click()
        current_color = context.driver.find_element(*curr_color).text
        print('Current color: ', current_color)
        actual_colors += [current_color]

    assert expected_colors == actual_colors, f'Expected {expected_colors}, but got {actual_colors}'
