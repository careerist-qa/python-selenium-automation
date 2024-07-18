from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

#Click SignIn button
driver.find_element(By.XPATH, '//span[contains(text(),"Sign in")]').click()

sleep(6)


#Click SignIn from side navigation
driver.find_element(By.XPATH, '//a[@data-test="accountNav-signIn"]').click()

#Verify SigIn page opened

sleep(6)


# verify
expected_text = 'Sign into your Target account'

actual_text = driver.find_element(By.XPATH, '//span[contains(text(),"Sign into your Target account")]').text
print(actual_text)
assert expected_text in actual_text, f'Expected text "{expected_text}" is not in "{actual_text}"'

print('Test case passed')