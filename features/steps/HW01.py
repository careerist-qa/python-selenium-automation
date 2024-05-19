
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

driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")
abcd = driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

driver.find_element(By.XPATH,"//input[@type='email']")

driver.find_element(By.XPATH,"//input[@id='continue']")

driver.find_element(By.XPATH,"//a[text()='Conditions of Use']")

driver.find_element(By.XPATH,"//a[@href='/gp/help/customer/display.html/ref=ox_signin_privacy?ie=UTF8&amp;nodeId=468496']")

driver.find_element(By.XPATH,"//input[@name='metadata1']")

driver.find_element(By.XPATH,"//a[@id='createAccountSubmit']")

driver.find_element(By.XPATH,"//select[@aria-describedby='searchDropdownDescription']")
driver.find_element(By.XPATH,"//select[@class='nav-search-dropdown searchSelect nav-progressive-attribute nav-progressive-search-dropdown']")'
driver.find_element(By.XPATH,"//a[text()='/gp/bestsellers/?ref_=nav_cs_bestsellers' and 'class='nav-a  ']")

