from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

# open the url
driver.get('https://www.target.com/')

# Click Account Button
driver.find_element(By.XPATH,  "//a[@data-test='@web/AccountLink']").click()
driver.find_element(By.XPATH, "//*[text()='Account']").click()
driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()

# Verify Sign-in page open
expected_text = 'Sign in or create account'
actual_text = driver.find_element(By.XPATH,"//*[text()='Sign in or create account']")
assert expected_text == actual_text, f'Expect text{expected_text} did not match actual text {actual_text}'

# Make sure login button is shown
driver.find_element(By.ID, 'login')


driver.quit()



#