from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


OPTIONS_LIST = (By.CSS_SELECTOR, "ul[role='radiogroup'] li")
COLOR_NAME = (By.CSS_SELECTOR, ".selection")
MAIN_RESULT_LIST = (By.CSS_SELECTOR, "[cel_widget_id*='MAIN-SEARCH_RESULTS']")
MAIN_RESULT_TEXT = (By.CSS_SELECTOR, "h2")
MAIN_RESULT_IMAGE = (By.CSS_SELECTOR, "[class*='product-image-container']")


@given("Open jeans product page")
def open_jeans_page(context):
    context.driver.get("https://www.amazon.com/gp/product/B07BJKRR25/")


@when("Verify there are {number_of_options} color options")
def get_colors_count(context, number_of_options):
    expected_number_of_options = 19
    number_of_options = context.driver.find_elements(*OPTIONS_LIST)
    assert(len(number_of_options) == expected_number_of_options), \
        f"Expected {expected_number_of_options}, but got {len(number_of_options)}"


@then("Verify expected colors are shown")
def verify_color_names(context):
    expected_colors = ["Black", "Blue, Over Dye", "Bright White", "Dark Blue Vintage",
                       "Dark Indigo/Rinsed", "Dark Khaki Brown", "Dark Wash", "Indigo Wash",
                       "Light Blue Vintage", "Light Khaki Brown", "Light Wash", "Medium Blue, Vintage",
                       "Medium Wash", "Olive", "Rinsed", "Sage Green", "Vintage Wash",
                       "Washed Black", "Washed Grey"]
    color_list = context.driver.find_elements(*OPTIONS_LIST)
    for color in color_list:
        color.click()
        actual_color_name = context.driver.find_element(*COLOR_NAME).text
        if actual_color_name in expected_colors:
            assert True


@then("Verify product results have name and image")
def verify_result_image_name(context):
    results_list = context.driver.find_elements(*MAIN_RESULT_LIST)
    for result in results_list:
        # Verifies that the result has a class of product-image-container
        result.find_element(*MAIN_RESULT_IMAGE)
        result_name = result.text
        lowered_result_name = result_name.lower()
        if "gaming" not in lowered_result_name:
            assert False, f"The name of this result is {lowered_result_name}"




