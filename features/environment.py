from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.hw6application import Hw6Application
from app.hw7_target_application import Hw7Application
from app.hw8_target_application import HW8Application


def browser_init(context):
    """
    :param context: Behave context
    """
    option_browser = 'Safari_BrowserStack'

    driver_path_chrome = ChromeDriverManager().install()
    service_chrome = Service(driver_path_chrome)
    service_edge = Service(
        executable_path='/Users/jkwak/Desktop/QA/python-selenium-automation/drivers/msedgedriver')
    service_firefox = Service(
        executable_path='/Users/jkwak/Desktop/QA/python-selenium-automation/drivers/geckodriver')

    ### Browser Options ###
    if option_browser == 'Chrome':
        context.driver = webdriver.Chrome(service=service_chrome)
    elif option_browser == 'Safari':
        context.driver = webdriver.Safari()
    elif option_browser == 'Edge':
        context.driver = webdriver.Edge(service=service_edge)
    elif option_browser == 'Firefox':
        context.driver = webdriver.Firefox(service=service_firefox)
    elif option_browser == 'Chrome_Headless':
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        context.driver = webdriver.Chrome(
            service=service_chrome,
            options=options
        )
    elif option_browser == 'Safari_BrowserStack':
        bs_user = 'justinkwak_4VEnze'
        bs_key = 'XrkEqEtBuz4zsM5Hs2xJ'
        url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'

        options = Options()
        bstack_options = {
            # 'os' : 'windows',
            # 'osVersion': '11',
            'os': 'OS X',
            'osVersion': 'sonoma',
            'browserName': 'safari',
            'sessionName': 'HW8 Test Scenario'
        }
        options.set_capability('bstack:options', bstack_options)
        context.driver = webdriver.Remote(command_executor=url, options=options)
    else:
        context.driver = webdriver.Chrome(service=service_chrome)

    context.driver.maximize_window()
    context.driver.implicitly_wait(10)  # It is a global function, so it works in all once it called once from anywhere
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.hw6app = Hw6Application(context.driver)
    context.hw7app = Hw7Application(context.driver)
    context.hw8app = HW8Application(context.driver)


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

