from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BEST_SELLERS_BTN = (By.CSS_SELECTOR, "a[data-csa-c-content-id='nav_cs_bestsellers']")
BEST_SELLERS_HEADER_LINKS = (By.CSS_SELECTOR, "div[class*='nav-tab-all_style'] a")
CUSTOMER_SERVICE_BTN = (By.CSS_SELECTOR, "#nav-xshop a[href*='customerservice']")
CUSTOMER_SERVICE_PAGE_MESSAGE = (By.CSS_SELECTOR, "h1[class='fs-heading bolded']")
ELEMENTS_IN_CONTAINER = (By.CSS_SELECTOR, ".issue-card-container .issue-card-wrapper")
CUSTOMER_SERVICE_SEARCH_BOX = (By.CSS_SELECTOR, "#hubHelpSearchInput")
SEARCH_LIBRARY_MESSAGE = (By.XPATH, "//h2[contains(text(),'Search our help library')]")
ALL_HELP_TOPICS_MESSAGE = (By.XPATH, "//h2[contains(text(),'All help topics')]")
HELP_TOPICS_NUMBER = (By.CSS_SELECTOR, ".help-topics-list-wrapper .help-topics")


@when("Click best sellers button")
def click_best_sellers_btn(context):
    context.driver.find_element(*BEST_SELLERS_BTN).click()


@when("Click Customer Service button")
def click_customer_service_button(context):
    context.driver.find_element(*CUSTOMER_SERVICE_BTN).click()


@then("Verify {links_number} best sellers header links")
def verify_best_sellers_links(context, links_number):
    links_number = int(links_number)
    page_links = len(context.driver.find_elements(*BEST_SELLERS_HEADER_LINKS))
    assert page_links == links_number, f"Expected {links_number}, but found {page_links} links"


@then("Verify Welcome to Amazon Customer Service Message")
def verify_hello_message(context):
    expected_message = "Welcome to Amazon Customer Service"
    customer_service_message = context.driver.find_element(*CUSTOMER_SERVICE_PAGE_MESSAGE).text
    assert customer_service_message == expected_message, f"Expected {expected_message}, but found " \
                                                         f"{CUSTOMER_SERVICE_PAGE_MESSAGE}"


@then("Verify {expected_container_count} items in container")
def customer_service_container_count(context, expected_container_count):
    expected_container_count = int(expected_container_count)
    actual_container_count = len(context.driver.find_elements(*ELEMENTS_IN_CONTAINER))
    assert actual_container_count == expected_container_count, f"Expected {expected_container_count}, but found " \
                                                               f"{actual_container_count}"


@then("Verify customer service search box")
def verify_cs_search_box(context):
    context.driver.find_element(*CUSTOMER_SERVICE_SEARCH_BOX)


@then("Verify search our help library message")
def verify_search_library_message(context):
    expected_message = "Search our help library"
    search_library_message = context.driver.find_element(*SEARCH_LIBRARY_MESSAGE).text
    assert search_library_message == expected_message, f"Expected {expected_message}, " \
                                                       f"but found {search_library_message}"


@then("Verify all help topics message")
def verify_all_help_topics(context):
    expected_message = "All help topics"
    actual_message = context.driver.find_element(*ALL_HELP_TOPICS_MESSAGE).text
    assert expected_message == actual_message, f"Expected {expected_message}, but found {actual_message}"


@then("Verify {topics_number} help topics")
def verify_help_topics_numbers(context, topics_number):
    topics_number = int(topics_number)
    help_topics_list_number = len(context.driver.find_elements(*HELP_TOPICS_NUMBER))
    assert help_topics_list_number == topics_number, f"Expected {topics_number} help topics," \
                                                     f"but found {help_topics_list_number}"


num = 35231
num_list = [i for i in str(num)]
final_list = [i for i in reversed(num_list)]
print(final_list)
