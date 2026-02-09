
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

##  aria-label="color,
COLOR_OPTIONS = (By.CSS_SELECTOR, 'ul li[class="styles_ndsCarouselItem__dnUkr"]')

SELECTED_COLOR = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] [class*="styles_headerWrapper"]')

# @when('Click on each color')
# def click_on_color(context):
#     context.driver.find_elements(By.CSS_SELECTOR, '.color').click()
#     sleep(2)


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    sleep(8)



@then('Click through colors and verify selection')
def verify_color(context):
    sleep(5)
    expected_colors = ['Berry Pink', 'Charcoal Gray', 'Light Beige']
    actual_colors = []
    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(len(colors))
    for color in colors[0:3]:
        sleep(5)
        color.click()
        selected_color = context.driver.find_element(*SELECTED_COLOR).text[6:]  # 'Color\nBlack'
        print('Current color', selected_color)
        #selected_color = selected_color.split('color\n39063-')[1] # remove 'Color\n' part, keep Black'
        sleep(3)
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'