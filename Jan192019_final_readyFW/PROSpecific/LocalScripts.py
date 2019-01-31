from selenium import webdriver
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.utils import *
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from time import sleep
from GenricScrits import genricSci as gn

global oBrowser
oBrowser=webdriver.Chrome()
oBrowser.maximize_window()


def kwdLogin(TestValues):
    Username=TestValues[1]
    Password=TestValues[2]

    oBrowser.get("http://localhost/login.do")
    sleep(2)
    oBrowser.find_element_by_xpath("//input[@id='username']").send_keys(Username)
    sleep(2)
    oBrowser.find_element_by_xpath("//input[@name='pwd']").send_keys(Password)
    sleep(2)
    oBrowser.find_element_by_xpath("//a[@id='loginButton']").click()
    sleep(1)
    webdriver.Chrome().close()


def RCTLogin(TestValues):
    for i in TestValues:
        print(i)

    print("Testing for 2 nd row and data")