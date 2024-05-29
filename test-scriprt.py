from selenium.webdriver.common.by import By
from selenium import webdriver
import json
import webdriver_manager


executor_object = {
    'action': 'setSessionName',
    'arguments': {
        'name': "<test-name>"
    }
}
browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
webdriver.execute_script(browserstack_executor)