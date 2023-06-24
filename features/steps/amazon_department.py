from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.ui import Select


SEARCH_ITEM = (By.CSS_SELECTOR,"#twotabsearchtextbox")
PRESS_SEARCH_ICON = (By.CSS_SELECTOR,"#nav-search-submit-button")
DEPARTMENT_SECTION = (By.ID,"searchDropdownBox")
APPLIANCES_LOCATOR = (By.CSS_SELECTOR,"a[href *='topnav_storetab_la']")


@given('Enter Amazon web page')
def open_google(context):
    context.driver.get('https://www.amazon.com/')
    sleep(5)

@when('choose the department {department_name} in department section')
def choose_department(context,department_name):
    select = Select(context.driver.find_element(*DEPARTMENT_SECTION))
    print(department_name)
    #select.select_by_index(6)
    select.select_by_value(department_name)
    sleep(2)


@then('enter item {search_word}search field')
def enter_item_search_field(context,search_word):
     search_field=context.driver.find_element(*SEARCH_ITEM)
     search_field.clear()
     search_field.send_keys(search_word)
     sleep(2)

@then('press the search icon')
def press_search_icon(context):

    context.driver.find_element(*PRESS_SEARCH_ICON).click()
    sleep(2)
    #context.app.main_page.click(*SEARCH_ICON_BUTTON)


@then("confirming given product result page brought from selected {department}")
def choose_departmentname_match_departmentsection(context,department):
    context.driver.find_element(*APPLIANCES_LOCATOR)
    sleep(2)