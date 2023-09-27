from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ### OTHER BROWSERS ###
    #service = Service(executable_path= "/Users/jacobgrable/QA/python-selenium-automation/geckodriver")
    #context.driver = webdriver.Firefox(service=service)
    #context.driver = webdriver.Safari()




def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)



def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
