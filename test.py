# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep
#
# # get the path to the ChromeDriver executable
# driver_path = ChromeDriverManager().install()
#
# # create a new Chrome browser instance
# service = Service(driver_path)
# driver = webdriver.Chrome(service=service)
#
# driver.get("https://www.amazon.com/AmazonBasics-Matte-Keyboard-QWERTY-Layout"
#                    "/dp/B07WJ5D3H4/ref=sr_1_1_sspa?crid=1FVNUV7XN2ZHG&keywords=keyboard"
#                    "&qid=1683507854&sprefix=keyboard%2Caps%2C353&sr=8-1-spons&psc=1&spLa="
#                    "ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRjY3T0lLSTZNS04wJmVuY3J5cHRlZElkPUEwMTcxO"
#                    "Dg2MURDVzExVlZURTFXNyZlbmNyeXB0ZWRBZElkPUEwNDcwNjgzMUVIMlk5MUZSVzMwUSZ"
#                    "3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=")
#
# driver.find_element(By.ID, "add-to-cart-button").click()
# time.sleep(1)
#
# driver.find_element(By.ID, "nav-cart-count-container").click()
#
# text = driver.find_element(By.ID, "attach-accessory-cart-total-string").text
# print(text)






