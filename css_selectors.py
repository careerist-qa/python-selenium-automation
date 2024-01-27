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

# CSS, connect by ID
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox')  # same as driver.find_element(By.ID, 'twotabsearchtextbox')
# By class
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us.icp-nav-flag')
# By TAG + class / id / attr
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag-us.icp-nav-flag')
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')
# By attr
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][aria-label='Search Amazon']")
# tag + attr
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][aria-label='Search Amazon']")
# attr + class + id
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox.nav-input[placeholder='Search Amazon']")
# Partial attr: "*="
driver.find_element(By.CSS_SELECTOR, "[aria-describedby*='Dropdown']")
driver.find_element(By.CSS_SELECTOR, "[class*='search-dropdown']")
driver.find_element(By.CSS_SELECTOR, "[class*='search-dropdown'][aria-describedby*='Dropdown']")

# From parent => child, separate by space:
driver.find_element(By.CSS_SELECTOR, "#legalTextRow [href*='condition']")
