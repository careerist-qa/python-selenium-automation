from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")

# COLOR_OPTIONS = (By.CSS_SELECTOR, "div[aria-label='Carousel'] li img")
# SELECTED_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")


@given('Open target product {product_id} page')
def open_target(context, product_id):
    context.driver.get(f'https://www.target.com/p/{product_id}')
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(COLOR_OPTIONS)
    )


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Black', 'Gray', 'Khaki']
    actual_colors = []

    # @then('Verify user can click through colors')
    # def click_and_verify_colors(context):
    #    expected_colors = ['Blue Tint', 'Denim Blue', 'Marine', 'Raven']
    #    actual_colors = []

    # Wait for the color options to be visible
    colors = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located(COLOR_OPTIONS)
    )

    for color in colors:
        try:
            # Scroll into view to ensure it’s visible and ready to be clicked
            context.driver.execute_script("arguments[0].scrollIntoView(true);", color)

            # Use ActionsChains for safe clicking
            ActionChains(context.driver).move_to_element(color).click().perform()

            # Retrieve the selected color text
            selected_color = WebDriverWait(context.driver, 10).until(
                EC.visibility_of_element_located(SELECTED_COLOR)
            ).text
            print('Current color:', selected_color)

            # Extract the color name and append to actual colors
            selected_color = selected_color.split('\n')[1]
            actual_colors.append(selected_color)

        except Exception as e:
            print(f"Error clicking color: {e}")
            continue

    # Assert the colors match the expected list
    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'

