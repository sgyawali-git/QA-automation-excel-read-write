#import required Library area
import openpyxl
from testResult import excel_operation
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from selenium.webdriver.firefox.service import Service as FirefoxServices
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException

test_location = r"C:\Users\A C E R\PycharmProjects\Python Learning\swag_lab\test_Case\read.xlsx"

#function define for read excel

def read_excel():
    wb = openpyxl.load_workbook(test_location)
    ws = wb["Sheet1"]
    for col in ws.iter_rows(min_row=2, values_only=True):
        sn, test_summary, xpath, action, value = col[0], col[1], col[2], col[3], col[4]
        #print(sn, test_summary, xpath, action, value)
        action_definition(sn,test_summary,xpath,action,value)




#action define section ie. all the actiona are defined here:

def action_definition(sn,test_summary,xpath,action,value):
    if action == "open_browser":
        result, remarks = open_browser(value)

    elif action == "open_url":
        result, remarks = open_url(value)

    elif action == "verify_title":
        result, remarks = verify_title(value)

    elif action == "verify_text":
        result, remarks = verify_text(xpath,value)

    elif action == "input_text":
        result, remarks = input_text(xpath,value)

    elif action == "click":
        result, remarks = click(xpath)
    elif action == "quit_browser":
        result, remarks = quit_browser(action)

    else :
        result, remarks = "NOT TESTED", ""

    excel_operation.write_result(sn, test_summary, result, remarks)


def open_browser(value):
    global driver
    try:
        if value == "chrome":
             s = ChromeServices(ChromeDriverManager().install())
             driver = webdriver.Chrome(service=s)
             driver.maximize_window()
             driver.implicitly_wait(10)
             result, remarks = "pass",""

        elif value == "firefox":
             s = FirefoxServices(GeckoDriverManager().install())
             driver = webdriver.Firefox(service=s)
             driver.maximize_window()
             driver.implicitly_wait(10)
             result, remarks = "pass", ""

        else :
             result, remarks = "FAILED","NOT SUPPORTED"

    except Exception as ex :
        result, remarks ="FAILED",ex
    return result,remarks

def open_url(value):
    try:
        driver.get(value)
        result, remarks = "PASS",""
    except Exception as ex:
        result, remarks = "FAILed", ex
    return result, remarks

def verify_title(value):
    try:
        actual_title = driver.title
        try:
           assert actual_title == value
           result,remarks = "PASS",""

        except AssertionError:
            result, remarks = "FAILED", "Text doesnot match"

    except Exception as ex:
        result, remarks = "FAILed", ex
    return result, remarks



def verify_text(xpath,value):
    try:
        actual_text= driver.find_element(By.XPATH, xpath).text
        try:
            assert actual_text == value
            result,remarks = "PASS",""

        except AssertionError:
            result,remarks ="fail","text doesnt match"
    except Exception as ex:
        result, remarks = "FAILED",ex
    return result, remarks


def input_text(xpath,value):
    try:
        driver.find_element(By.XPATH, xpath).send_keys(value)
        result, remarks = "PASS", ""
    except Exception as ex:
        result, remarks = "FAILED", ex

    return result, remarks


def click(xpath):
    try:
        driver.find_element(By.XPATH, xpath).click()
        result, remarks = "PASS", ""
    except Exception as ex:
        result, remarks = "FAILED", ex
    return result, remarks



def quit_browser(action):
    try:
        driver.quit()
        result, remarks = "Browser close sucessfully", ""
    except Exception as ex:
        result, remarks = "FAILED", ex
    return result, remarks


excel_operation.remove_file()
excel_operation.create_excel()
read_excel()