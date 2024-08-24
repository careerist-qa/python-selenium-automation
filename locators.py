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

# By Xpath, text:
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, '//a[text()="Best Sellers"]')
# By Xpath, text and attributes:
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# By attributes or text only, any tag
driver.find_element(By.XPATH, "//*[@name='field-keywords']")
driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")

# By attributes, parent node => child
driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")
