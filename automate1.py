
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeServices
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.firefox.service import Service as FirefoxServices
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
s = ChromeServices(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)
driver.get("https://www.saucedemo.com/")
time.sleep(10)
#driver.find_element(By.XPATH,"//input[@name="user-name"]").send_keys("standard_user")
#driver.find_element(By.XPATH,"//input[@name="user-name"]").
driver.find_element(By.XPATH,' //input[@name="login-button"]').click()
#time.sleep(10)
errorr= None
try:

    errorr = driver.find_element(By.XPATH,'//div[@class="error-message-container error"]').text
    print(errorr)
    if errorr != None:
        print(errorr)
    else:
except NoSuchElementException :
    print('no error occurs')


driver.maximize_window()
driver.quit()