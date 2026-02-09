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

# CSS, by ID => #
driver.find_element(By.CSS_SELECTOR, '#twotabsearchtextbox') # (By.ID, 'twotabsearchtextbox')
# CSS, by ID and tag
driver.find_element(By.CSS_SELECTOR, 'input#twotabsearchtextbox')

# CSS, class => .
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag-us.icp-nav-flag')
driver.find_element(By.CSS_SELECTOR, '.icp-nav-flag.icp-nav-flag-us')
# CSS, class and tag
driver.find_element(By.CSS_SELECTOR, 'span.icp-nav-flag.icp-nav-flag-us')
# CSS, tag, id, class
driver.find_element(By.CSS_SELECTOR, "input#twotabsearchtextbox.nav-progressive-attribute")

# CSS, attributes => []
driver.find_element(By.CSS_SELECTOR, "[aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords']")
driver.find_element(By.CSS_SELECTOR, "[name='field-keywords'][aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input[name='field-keywords'][aria-label='Search Amazon']")

driver.find_element(By.CSS_SELECTOR, ".nav-input[name='field-keywords'][aria-label='Search Amazon']")
driver.find_element(By.CSS_SELECTOR, "input.nav-input[name='field-keywords'][aria-label='Search Amazon']")

# CSS, attributes, contains => *= []
driver.find_element(By.CSS_SELECTOR, "[aria-label*='Amazon']")
driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
driver.find_element(By.CSS_SELECTOR, "[class*='styles_ndsBaseButton'][class*='styles_ndsButtonPrimary']")
\