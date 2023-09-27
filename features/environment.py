from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Chrome(service=service)
    #service = Service(executable_path= "/Users/jacobgrable/QA/python-selenium-automation/geckodriver")
    #context.driver = webdriver.Firefox(service=service)
    context.driver = webdriver.Safari()

    ### BROWSERSTACK ###
     #Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    bs_user = 'jacobgrable_02vm1G'
    bs_key = 'qcMffBqrPwXHx1H7JwoH'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

    options = Options()
    bstack_options = {
         'os': 'MacOS',
         'osVersion': '13.4.1',
         'browserName': 'Safari',
         'sessionName': scenario_name
     }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 1)

    context.app = Application(context.driver)


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
