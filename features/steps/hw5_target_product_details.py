from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
import re
import time

AD_CONTAINER_ID = (By.ID, 'btf')
COLOR_OPTIONS = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] picture img')
ALL_SELECTED_DIVS = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] div')


@given('Open target product {product_id} page')
def open_target_product_details_page(context, product_id):
    context.tic = time.time()
    context.base_page_url = "https://www.target.com/p/"
    context.driver.get(context.base_page_url + product_id)


@then('Verify user can click through {colors}')
def verify_selected_colors(context, colors):
    context.driver.wait.until(EC.visibility_of_element_located(AD_CONTAINER_ID))   # To wait for adContainer pop up
    context.driver.refresh()    # To overcome StaleElementReferenceException by getting a new element reference

    print(f'Expected colors: {colors}')
    actual_colors = []
    sleep(1)    # 2nd product detail page has another blocker and I couldn't find out a solution for the case yet.
    color_options = context.driver.find_elements(*COLOR_OPTIONS)
    for color_option in color_options:
        color_option.click()
        all_selected_divs = context.driver.find_elements(*ALL_SELECTED_DIVS)

        # I couldn't find out how to locate only the div.text including span.text "color"
        for selected_div in all_selected_divs:
            # justin = selected_div.get_attribute("innerText")
            selected_div_text = selected_div.text
            if "color" in selected_div_text.lower():
                # The last color of 1st product is Out of Stock.
                selected_color = re.sub(r' .*tock.*', '', selected_div_text.split('\n')[1])
                actual_colors.append(selected_color)

    print(f'Actual colors: {actual_colors}')
    assert str(actual_colors) == colors, f'Expected {colors} did not match actual {actual_colors}'
    tok = time.time()
    elapsed_time = tok - context.tic
    print(f'Elapsed time: {elapsed_time:.2f} seconds')





        # selected_elements = context.driver.find_elements(*SELECTED_COLOR)
        # for e in selected_elements:
        #     selected_color = e.text
        #     print(f'Selected color: {selected_color}')
        #context.driver.wait.until(EC.visibility_of_element_located(COLOR_TEXTS))

    sleep(2)



