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
#Amazon logo
driver.find_element(By.XPATH, "//i[@aria-label='Amazon']")

#Email field
driver.find_element(By.XPATH, "//input[@id='ap_email']")

# Continue button
driver.find_element(By.XPATH, "//input[@id='continue']")
#Conditions of use link and Privacy Notice link
driver.find_element(By.XPATH,  "//*[@id='legalTextRow']/a[1]" and "//*[@id='legalTextRow']/a[2]")
#Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")
#FYI I don't have "Forgot your password link and Other issue with Sign-in link"

#Create your Amazon account button
driver.find_element(By.XPATH, "//a[@id='createAccountSubmit']")


