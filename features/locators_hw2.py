from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fgp%2Fcart%2Fview.html%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

sleep(10)

####LOCATORS
#Amazon Logo
driver.find_element(By.CSS_SELECTOR, '[class="a-icon a-icon-logo"]')

#Email field
driver.find_element(By.CSS_SELECTOR,'[class="a-input-text"]')

#Continue button
driver.find_element(By.CSS_SELECTOR, '[class="a-button-input"]')

#Conditions of use link
driver.find_element(By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html/ref=ap_signin_notification_condition_of_use"]')

#Privacy Notice link
driver.find_element(By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html/ref=ap_signin_notification_privacy_notice"]')

#Need help link
driver.find_element(By.CSS_SELECTOR, '[class="a-size-base a-link-normal"]')


driver.quit()










#
#
# # By ID
# driver.find_element(By.ID, 'twotabsearchtextbox')
# driver.find_element(By.ID, 'nav-search-submit-button')
#
# # By Xpath
# driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']") # //tag[@attr='value']
# driver.find_element(By.XPATH, "//input[@role='searchbox']")
#
# # By Xpath, multiple attributes
# driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords']")
# driver.find_element(By.XPATH, "//input[@tabindex='0' and @name='field-keywords' and @role='searchbox']")
# driver.find_element(By.XPATH, "//input[@name='field-keywords' and @tabindex='0' and @role='searchbox']")
#
# # By Xpath, any tag
# driver.find_element(By.XPATH, "//*[@aria-label='Search Amazon']")
#
# # By Xpath, using text
# driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
# driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")
# driver.find_element(By.XPATH, "//a[@class='nav-a  ' and text()='Best Sellers']")
#
# # partial text match
# driver.find_element(By.XPATH, "//h2[contains(text(), 'Luxury')]")
# # partial attr match
# driver.find_element(By.XPATH, "//select[contains(@class, 'nav-search-dropdown')]")