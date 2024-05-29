from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
import time



driver_path = ChromeDriverManager().install()

# init driver
driver = webdriver.Edge()

driver.get("https://www.target.com/")

driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()

driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn' and @href='/account']").click()

sleep(4)

driver.find_element(By.ID, 'login').text
expected_result = 'Sign into your Target account'
actual_result = driver.find_element(By.XPATH, "//h1[@class='styles__StyledHeading-sc-1xmf98v-0 styles__AuthHeading-sc-kz6dq2-2 jhKFiw kcHdEa']").text
assert expected_result == actual_result, f'Expected "{expected_result}" but got "{actual_result}"'

print("Test Passed")