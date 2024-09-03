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

driver.get("https://www.target.com/")

# search key => enter coffee
driver.find_element(By.ID, 'search').send_keys('coffee')
# search button => click
driver.find_element(By.XPATH,"//button[@data-test='@web/Search/SearchButton']").click()
#Wait for search to complete
sleep(5)

# verification
#After wait find what you are looking for
actual_result = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text

expected_result ='coffee'

assert expected_result in actual_result
print('Test case passed')