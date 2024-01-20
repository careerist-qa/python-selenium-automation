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
search_word = 'coffee'

# Input search word
driver.find_element(By.ID, 'search').send_keys(search_word)

# Click on search btn
driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
sleep(6)

# Verify search worked:
actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert search_word in actual_text, f'Expected word {search_word} not in {actual_text}'

print('Test case passed')
driver.quit()
