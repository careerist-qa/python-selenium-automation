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

# Find by css, using id:
driver.find_element(By.CSS_SELECTOR, "#twotabsearchtextbox") # driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox")

# Find by css, using classes:
driver.find_element(By.CSS_SELECTOR, ".nav-input")
driver.find_element(By.CSS_SELECTOR, ".nav-progressive-attribute.nav-input")
# tag + classes
driver.find_element(By.CSS_SELECTOR, "input.nav-progressive-attribute.nav-input")
# tag + id + classes
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-progressive-attribute.nav-input")
# attributes:
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")
driver.find_element(By.CSS_SELECTOR, "[placeholder='Search Amazon'][type='text']")
# tag + attributes
driver.find_element(By.CSS_SELECTOR, "input[placeholder='Search Amazon'][type='text']")
# tag + #id + .class + [attributes]
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-input[placeholder='Search Amazon'][type='text']")
# Order doesn't matter (although it's recommended to have: tag + #id + .class + [attributes])
driver.find_element(By.CSS_SELECTOR, "input[type='text'].nav-input[placeholder='Search Amazon']#twotabsearchtextbox")

# Attributes, partial match
driver.find_element(By.CSS_SELECTOR, "[placeholder*='Search Ama']")
driver.find_element(By.CSS_SELECTOR, "a[href*='ap_signin_notification_privacy_notice']")
driver.find_element(By.CSS_SELECTOR, "a[class*='ap_signin_notification_privacy_notice']")

# Multiple nodes,  parent => child
driver.find_element(By.CSS_SELECTOR, "div.a-box div#legalTextRow a[href*='condition']")








