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

driver.get("https://www.target.com/")

# find and click sign in button
driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']").click()
sleep(10)
# click SignIn from side navigation
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(10)
# verification for “Sign into your Target account” text is shown
driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")
# verification for SignIn button is shown
driver.find_element(By.XPATH, "//button[@type='submit']")
