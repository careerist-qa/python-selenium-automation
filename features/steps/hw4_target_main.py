from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@given('Open target.com')
def open_target_com(context):
    context.driver.get('https://www.target.com')


@when('Input {product} in input search')
def input_product_search(context, product):
    search_input = context.driver.find_element(By.ID, 'search')
    search_input.send_keys(product)


@when('Click button search')
def click_button_search(context):
    context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]').click()
    sleep(2)


@when('Wait for a banner to unblock')
def wait_for(context):
    sleep(8)


@when('Open the target circle page')
def open_circle_page(context):
    context.driver.find_element(By.ID, 'utilityNav-circle').click()


@when('Clear input search')
def clear_input_search(context):
    search_input = context.driver.find_element(By.ID, 'search')
    len_previous_search_input = len(search_input.get_attribute('value'))
    i = 0
    if len_previous_search_input > 0:
        while i < len_previous_search_input:
            search_input.send_keys(Keys.BACK_SPACE)
            i += 1


@when('Open Help page')
def open_help_page(context):
    # Scroll to the Primary Footer div
    sleep(5)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    primary_footer_div = context.driver.find_element(By.CSS_SELECTOR, '[data-test="@web/component-footer/PrimaryFooter"]')
    actions = ActionChains(context.driver)
    actions.move_to_element(primary_footer_div).perform()

    # Locate
    link_help_page = context.driver.find_element(By.CSS_SELECTOR, '[href="https://help.target.com/help"]')
    # Click the element
    link_help_page.click()
    sleep(2)
