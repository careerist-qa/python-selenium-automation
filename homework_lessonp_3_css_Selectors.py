from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Amazon icon
driver.find_element(By.CSS_SELECTOR, ("[aria-label='Amazon']")

# create account icon
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# your name
driver.find_element(By.CSS_SELECTOR, "[placeholder='First and last name']")

# email
driver.find_element(By.CSS_SELECTOR, "[name='email']" )

# password
driver.find_element(By.CSS_SELECTOR, "[name='password']")

#password must be at least 6 characters
driver.find_element(By.CSS_SELECTOR, '.auth-inline-information-message div.a-alert-content.')

# re-enter password
driver.find_element(By.CSS_SELECTOR, "[name='passwordCheck']")

#continue Button
driver.find_element(By.CSS_SELECTOR, '#continue')

#conditions of use
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condit']")

#privacy notice
driver.find_element(By.CSS_SELECTOR, "a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privac']")

#sign in
driver.find_element(By.CSS_SELECTOR, "a[href*='/ap/signin?openid.pape.max_auth_age']")
