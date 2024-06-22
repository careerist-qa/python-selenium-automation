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

driver.get('https://www.target.com/')

# find search field and enter text
driver.find_element(By.ID, 'search').send_keys('tea')
# click search
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

# wait for the page with search results to load
sleep(6)

# verify
expected_text = 'tea'
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
# print(actual_text)
assert expected_text in actual_text, f'Expected text {expected_text} is not in actual text {actual_text}'

print('Test case passed')
driver.quit()
