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
driver.get('https://www.target.com/')

#click signin
driver.find_element(By.XPATH, "//span[@class='styles__LinkText-sc-1e1g60c-3 dZfgoT h-margin-r-x3']").click()

sleep(3)
#click signin from side bar
driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()
sleep(3)
#Verify “Sign into your Target account” text is shown

actual_text = driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/h1/span[text()='Sign into your Target account']").text

print(actual_text)


#Verify SignIn button is shown
driver.find_element(By.XPATH, "//button[@type='submit']")
