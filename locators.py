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

driver.get('https://www.amazon.com/')

# search by ID
driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'twotabsearchtextbox')

# search by XPath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")
# by XPath, multiple attributes
driver.find_element(By.XPATH, "//input[@class='nav-input nav-progressive-attribute' and @value='Go']")
driver.find_element(By.XPATH, "//input[@value='Go' and @class='nav-input nav-progressive-attribute' and @type='submit']")

# search by XPath, text()
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
# contains()
driver.find_element(By.XPATH,"//h2[contains(text(), 'Scary-good')]")
driver.find_element(By.XPATH,"//input[contains(@aria-label, 'Search ')]")

# From parent to child
driver.find_element(By.XPATH, "//div[@id='nav-main']//a[text()='Best Sellers']")