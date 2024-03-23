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

# By IDs
driver.find_element(By.ID, 'twotabsearchtextbox')

# By XPATH
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
# by multiple attr
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @type='text' and @name='field-keywords']")
# by text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# by text and attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
# any tag + by text and attributes
driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")
# contains()
driver.find_element(By.XPATH, "//select[contains(@class, 'search-dropdown')]")
driver.find_element(By.XPATH, "//*[contains(@class, 'search-dropdown')]")
driver.find_element(By.XPATH, "//*[contains(@class, 'search-dropdown') and ...]")













