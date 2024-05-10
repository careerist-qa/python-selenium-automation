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

driver.get('http://www.target.com/')

driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()

driver.find_element(By.XPATH, "//*[@id='listaccountNav-signIn']/a/span").click()
sleep(6)
actual_text = driver.find_element(By.XPATH, "//*[@id='__next']/div/div/div/div[1]/div/h1/span").text
#Sign in button
driver.find_element(By.XPATH, "//button[@type='submit']")

driver.quit()