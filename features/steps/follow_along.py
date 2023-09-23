from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then, given

def sum_of_three_digit_number(number: int):
    result = 0
    for i in range(3):
        current_number = number % 10
        result = result + current_number
        number = number // 10
    return result

test_result = sum_of_three_digit_number(354)
print(test_result)