
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# init driver
# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(4)

# open the url
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')

# Switch to frame 1
driver.switch_to.frame('iframeResult')

# Switch to frame 2
frame2 = driver.find_element(By.CSS_SELECTOR, "iframe[src='https://www.w3schools.com']")
driver.switch_to.frame(frame2)

login = driver.find_element(By.ID, 'w3loginbtn')
print(login.get_attribute('title'))

assert login.get_attribute('title') == 'Login to your account', \
    f"Title is {login.get_attribute('title')} instead of Login to your account"

driver.quit()
