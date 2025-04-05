from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

# By Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']") # //tag[@attr='value']
driver.find_element(By.XPATH, "//input[@role='searchbox']")

# By Xpath, multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @role='searchbox']")
driver.find_element(By.XPATH, "//input[@name='field-keywords' and @tabindex='0' and @role='searchbox']")

# By Xpath, any tag
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")

# By Xpath, using text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and text()='Best Sellers']")

# partial text match
driver.find_element(By.XPATH, "//h2[contains(text(), 'Luxury')]")
# partial attr match
driver.find_element(By.XPATH, "//select[contains(@class, 'nav-search-dropdown')]")