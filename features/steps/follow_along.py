from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import when, then, given

def find_missing_element(arr1: list, arr2: list):
    arr1.sort()
    arr2.sort()

    for i in range(len(arr2) -1):
        if arr1[i] != arr2[i]:
            print(str(arr1[i]) + ' is the missing element ')
            return
    print(str(arr1[-1]) + ' is the missing element')

testlist1 = [1, 3, 2, 4, 5, 7, 9]
testlist2 = [3, 2, 1, 5, 9, 7]
find_missing_element(testlist1, testlist2)

