from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BEST_SELLER_LINK = (By.CSS_SELECTOR, 'div._p13n-zg-nav-tab-all_style_zg-tabs__EYPLq a')



@given( 'Open Amazon Bestseller page')
def open_amazon_best_seller(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
    sleep(10)
@then('Confirm {link_count} links exist')
def confirm_links_exist(context, link_count):
    all_links_count = len(context.driver.find_elements(*BEST_SELLER_LINK))
    #to compare  actual result with expected result
    print("all products count",all_links_count,type(all_links_count))
    print("expected links count",int(link_count),type(int(link_count)))
    assert int(link_count) == all_links_count, f'Expected link count {link_count}  does not match actual link count {all_links_count}'
