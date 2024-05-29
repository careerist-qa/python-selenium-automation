from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

# By ID
driver.find_element(By.ID, 'twotabsearchtextbox')

# By Xpath
driver.find_element(By.XPATH, "//a[@href='/ref=nav_logo']")
driver.find_element(By.XPATH, "//input[@aria-label='Search']")
driver.find_element(By.XPATH, "//input[@name='field-keywords']")

# By Xpath, multiple attributes
driver.find_element(By.XPATH, "//input[@tabindex='0' and @aria-label='Search']")
driver.find_element(By.XPATH, "//input[@tabindex='0' and @aria-label='Search' and @another_attribute....]")

# By Xpath, text
driver.find_element(By.XPATH, "//h2[text()='Deals on overstock items']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @data-csa-c-content-id='nav_cs_bestsellers']")

# By Xpath, partial attribute
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//span[contains(text(), 'BELLA 21 Piece Cook Bake')]")  # by partial text

# By Xpath, multiple nodes
driver.find_element(By.XPATH, "//div[@id='nav-xshop-container']//a[contains(@href, 'bestsellers')]")
