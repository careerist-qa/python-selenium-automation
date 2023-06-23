from  selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
#SEARCH_INPUT = (By.NAME, 'q')
NEW_ARRIVALS = (By.CSS_SELECTOR,"a[href*='sv_sl_6']")
MEN_DEALS = (By.CSS_SELECTOR,"a[href*='sv_sl_na_2']")
# NEW_ARRIVALS = (By.CSS_SELECTOR,'a[href*="sv_sl_6"]')
# MEN_DEALS = (By.CSS_SELECTOR,'a[href*="sv_sl_na_2"]')

@given('Enter Amazon product page')
def enter_amazon_product_page(context):
    context.driver.get('https://www.amazon.com/gp/product/B074TBCSC8')
    sleep(15)


@when('Mouse hover over NewArrivals')
def mouse_hover_over_newarrivals(context):
    actions = ActionChains(context.driver)

    new_arrivals_element =context.driver.find_element(*NEW_ARRIVALS)
    actions.move_to_element(new_arrivals_element)
    actions.perform()
    sleep(3)


@then('confirm that men deal is shown')
def deals_page_shown(context):
   context.driver.find_element(*MEN_DEALS)


