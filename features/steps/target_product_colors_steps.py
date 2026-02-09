from behave import then, given
from selenium.webdriver.common.by import By
from time import sleep



@given('Open target product A-94089062 page')
def open_target(context):
    context.driver.get('https://www.target.com/p/josmo-boys-slip-on-casual-boat-style-shoes-little-kids-toddler-tan-size-10/-/A-94089062')
    sleep(5)


@then('Verify that every product color is clicked and correct')
def verify_product_color_is_clicked_correct(context):
    expected_colors = ['black', 'tan']
    actual_colors = []


    COLOR_CHOICES = (By.CSS_SELECTOR, 'a[class*="styles_ndsBaseButton"] img[class*="styles_pictureLazy"]')
    SELECTED_COLOR = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] div[class*="styles_headerWrapper"]')

    colors = context.driver.find_elements(*COLOR_CHOICES)
    print(colors)


    for color in colors:
        color.click()
        sleep(10)

        selected_color = context.driver.find_elements(*SELECTED_COLOR)[1].text

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)

    assert expected_colors == actual_colors, f"Expected colors are: ({expected_colors}), but got Actual colors: ({actual_colors}) "



