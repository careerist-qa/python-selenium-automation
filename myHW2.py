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
# to click sign in page from amazon.com
mySignIn=driver.find_element(By.ID,'nav-link-accountList-nav-line-1')
#wait for 5 seconds for see the cursor moving
sleep(5)

mySignIn.click()
sleep(5)
#move cursor over amazon logo
driver.find_element(By.XPATH,"//i[@class='a-icon a-icon-logo']")
sleep(5)
#move cursor over te mobile or email text box
myEmailText=driver.find_element(By.ID,'ap_email')
#put information bharathigajan@gmail.com in email text box
myEmailText.send_keys('bharathigajan@gmail.com')
#Need help
driver.find_element(By.CLASS_NAME,'a-expander-prompt')
sleep(5)
#Forgot password
driver.find_element(By.ID,'auth-fpp-link-bottom')
sleep(5)
#Other issues
driver.find_element(By.ID,'ap-other-signin-issues-link')
sleep(5)
#condition of use
driver.find_element(By.XPATH,"//a[contains(@href,notification_privacy_notice)]")
sleep(5)
#PRIVACY
driver.find_element(By.XPATH,"//a[contains(@href,privacy)]")
sleep(5)
#Createyouramazonaccount
driver.find_element(By.ID,'createAccountSubmit')
sleep(5)

#condition of use
#$x("//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use?ie=UTF58&nodeId=508088']")
#privacy
#$x("//a[@href='/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice?ie=UTF8&nodeId=468496']")


#click the continue button
driver.find_element(By.ID,'continue')

driver.quit()

