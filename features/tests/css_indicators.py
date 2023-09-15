from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

#amazon logo
webdriver.find_element(By.CSS_SELECTOR, '.a-icon.a-icon-logo')

#create account button
webdriver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

# your name field
webdriver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

# email field
webdriver.find_element(By.CSS_SELECTOR, '#ap_email')

# password field
webdriver.find_element(By.CSS_SELECTOR, '#ap_password')

#password information text
webdriver.find_element(By.XPATH, "//div[contains(text(), '  Passwords must be at least 6 characters.')]")

# reenter password
webdriver.find_element(By.CSS_SELECTOR, '#ap_password_check')

# continue button
webdriver.find_element(By.CSS_SELECTOR, '#continue')

# conditions of use link
webdriver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use') and @href ='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088']")

#privacy notice
webdriver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice') and @href ='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?ie=UTF8&nodeId=468496']")

# sign in button
webdriver.find_element(By.CSS_SELECTOR, "[class=a-link-emphasis][href*='/ap']")
