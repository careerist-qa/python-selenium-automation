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

# Locate element:
# driver.find_element() # By. / value
# Locate by ID:
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-logo-sprites')

# By Xpath, using 1 attribute
driver.find_element(By.XPATH, "//img[@alt='Shop Studio Pro headphones']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
# By Xpath, multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @href='/gp/bestsellers/?ref_=nav_cs_bestsellers' and @tabindex='0']")