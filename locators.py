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

#open url for amazon.com
driver.get('https://www.amazon.com/')


#get relement by ID
driver.find_element(By.ID, 'twotabsearchtextbox')

#get relement by xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")