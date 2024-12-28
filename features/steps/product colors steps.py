from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@given("a specific product")
def product_page(context):
    context.driver.get("https://www.target.com/p/A-54551690")
sleep (3)


@then("Verify if product with specific color is displayed")
def verify_product_color(context):
     product_color = ["Blue Tint", "Denim Blue", "Raven", "Marine"]
     actual_colors = []

     colors = context.driver.find_elements(By.CSS_SELECTOR,"div[aria-label='Carousel']")

for color in colors:
    color.click()

    selected_colors= context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/VariationComponent'] div")
    print('Current color',selected_colors)

    selected_color = selected_color.split('\n')[1]  # remove 'Color\n' part, keep Black'
    actual_colors.append(selected_color)
    print(actual_colors)

assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'








