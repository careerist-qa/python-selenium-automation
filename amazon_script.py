from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
# driver.implicitly_wait(4)
wait = WebDriverWait(driver, timeout=10)

# open the url
driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')
sleep(2)

links = driver.find_elements(By.CSS_SELECTOR, '#zg_header a')
print(links)

for i in range(len(links)):
    links = driver.find_elements(By.CSS_SELECTOR, '#zg_header a')
    links[i].click()
    sleep(2)
