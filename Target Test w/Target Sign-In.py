from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

# sign In
driver.find_element(By.XPATH, "//span[text()='Account']").click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# verify
expected = 'Sign in or create account'
actual = driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
assert expected == actual, f'Expected {expected} did not match actual {actual}'