from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get a path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open a url
driver.get('https://www.target.com/')
sleep(2)

sign_text = driver.find_element(By.XPATH, "//*[text()='Sign in']").text
print(sign_text)
