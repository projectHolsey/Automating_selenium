from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import requests
import time

driver = webdriver.Chrome('C:/Program Files/chromedriver_win32/chromedriver')
driver.get("https://summer.highland.gov.uk/connect/mrmlogin.aspx")

user = driver.find_element_by_name("ctl00$MainContent$InputLogin")
user.send_keys("Matty-sep@hotmail.com")
password = driver.find_element_by_name("ctl00$MainContent$InputPassword")
password.send_keys("Jasper3126")
password.send_keys(Keys.RETURN)

time.sleep(1)

driver.execute_script("document.getElementById('ctl00_MainContent__advanceSearchResultsUserControl_Activities_ctrl2_lnkActivitySelect_xs').click()")

time.sleep(1)

for i in range(6):
    driver.find_element_by_id("ctl00_MainContent_Button2").click()

# x = driver.find_element_by_id("ctl00_MainContent_grdResourceView")
print(driver.find_element_by_id("ctl00_MainContent_lblCurrentNavDate").text)
if any(elem in str(driver.find_element_by_id("ctl00_MainContent_lblCurrentNavDate").text).lower() for elem in ["mon","tue","wed","thu","fri"] ):
    try :
        driver.find_element_by_name("ctl00$MainContent$grdResourceView$ctl09$ctl00").click()

    except Exception as e:
        pass



    # ctl00$MainContent$grdResourceView$ctl09$ctl00
    # ctl00$MainContent$grdResourceView$ctl09$ctl01





driver.close()