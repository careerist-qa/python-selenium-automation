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
driver.get('https://www.amazon.com/')

# Locators
# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'searchDropdownBox')

driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute']")

# By attributes, any tag
driver.find_element(By.XPATH, "//*[@placeholder='Search Amazon']")

driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute' and @type='text']")
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute']")