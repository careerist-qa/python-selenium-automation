from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import webdriver_manager


executor_object = {
    'action': 'setSessionStatus',
    'arguments': {
        'status': "<passed/failed>",
        'reason': "<reason>"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
webdriver.execute_script(browserstack_executor).maximize_window()
