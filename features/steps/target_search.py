from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


driver_path = ChromeDriverManager().install()


service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()


driver.get('https://www.target.com/')


driver.find_element(By.ID, 'search').send_keys('bicycle')

driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()

sleep(6)


actual_text = driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
assert 'bicycle' in actual_text, f'Error! Text coffee not in {actual_text}'

driver.quit()
