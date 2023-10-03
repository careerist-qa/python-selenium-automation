from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page



# variables
FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescText')
SIGNIN_BTTN = (By.CSS_SELECTOR, '#nav-signin-tooltip .nav-action-signin-button')
SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
SEARCH_BTTN = (By.ID, 'nav-search-submit-button')


@given('Open Amazon page')
def open_amazon(context):
    # context.driver.get('https://amazon.com')
    context.app.main_page.open_main()
    sleep(2)
    context.driver.refresh()

@when('Open Hamburger Menu')
def open_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, 'i.hm-icon').click()

@then('Open Best Sellers Page')
def open_best_sellers_page(context):
    context.driver.find_element(By.CSS_SELECTOR, '[href*="=nav_em_cs_bestsellers_0_1_1"]').click()
    sleep(2)
    context.driver.refresh()


@when('Search for {product}')
def search_on_amazon(context, product):
    context.app.header.search_product(product)

@then('Verify footer has {expected_amount} links')
def verify_link_amount(context, expected_amount):
    expected_amount = int(expected_amount)
    links = context.driver.find_elements(*FOOTER_LINKS)
    print(links)
    print(f'Total links:{len(links)}')
    assert len(links) == expected_amount,f'Expected {expected_amount} links but got {len(links)}'

@when('Click on button from Sign-In popup')
def click_sign_in_popup(context):
    context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BTTN)).click()

@when('Verify Sign-in is clickable')
def verify_sign_in_btn_is_clickable(context):
    # context.driver.wait.until(EC.element_to_be_clickable(SIGNIN_BTTN),
    #  message= 'Sign in button not clickable')
    context.app.header.wait_for_element_clickable(*SIGNIN_BTTN)

@when('Wait for 3 seconds')
def wait_sec(context):
        sleep(3)

@then('Verify Sign-in disappears')
def verify_sign_in_btn_disappears(context):
        context.app.header.wait_for_element_disappear(*SIGNIN_BTTN)
