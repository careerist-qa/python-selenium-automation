from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Access amazon website
driver.get("https://www.amazon.com/")

# Click on orders button
driver.find_element(By.XPATH, "//a[@id='nav-orders']").click()

# Send text in email field to verify
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("Verification Complete")

driver.close()

print("Test Case Passed!")
