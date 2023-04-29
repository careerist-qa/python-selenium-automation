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

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'nav-search-submit-button')

# By Xpath
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")

# By Xpath, with quotes, exception:
driver.find_element(By.XPATH, "//img[@alt=\"Shopbop Mother's Day gifts\"]")

# By Xpath, multiple attributes
driver.find_element(By.XPATH, "//input[@name='field-keywords' and @placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//input[@placeholder='Search Amazon' and @name='field-keywords']")

# By Xpath, text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# By Xpath, text AND attr
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# By Xpath, contains
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sell')]")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sell') and @class='nav-a  ']")
driver.find_element(By.XPATH, "//a[contains(text(), 'Best Sell') and contains(@class, 'nav-a')]")

# By Xpath, from parent => to child
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//div[@id='nav-xshop']//a[text()='Best Sellers']")