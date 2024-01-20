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

# IDs:
driver.find_element(By.ID, 'twotabsearchtextbox')
driver.find_element(By.ID, 'searchDropdownBox')

# Xpath
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")

# Multiple attr
driver.find_element(By.XPATH, "//input[@tabindex='0' and @placeholder='Search Amazon']")
driver.find_element(By.XPATH, "//select[@class='nav-search-dropdown "
                              "searchSelect nav-progressive-attrubute nav-progressive-search-dropdown']")
# Partial attr => contains()
driver.find_element(By.XPATH, "//select[contains(@class,'search-dropdown')]")
driver.find_element(By.XPATH, "//select[contains(@class,'search-dropdown') and @ame='url']")

# text()
driver.find_element(By.XPATH, "//span[text()='Winter Sale deals for your home']")
# text() + attr
driver.find_element(By.XPATH, "//span[text()='Winter Sale deals for your home' and "
                              "@class='a-truncate-full a-offscreen']")

# text() + contains()
driver.find_element(By.XPATH, "//span[contains(text(), ' Sale deals for') and @class='a-truncate-full a-offscreen']")
