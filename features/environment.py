from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait   # Only for Explicit Waits
# Link Page app layer and BDD feature layer
from app.hw6application import Hw6Application
from app.hw7_target_application import Hw7Application


def browser_init(context):
    """
    :param context: Behave context
    """
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.driver.implicitly_wait(10)  # It is a global function, so it works in all once it called once from anywhere
    context.driver.wait = WebDriverWait(context.driver, 15)
    # Construct a global Hw6Application instance with webdriver.Chrome
    context.hw6app = Hw6Application(context.driver)
    context.hw7app = Hw7Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
