from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import requests
import time


driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
driver.get("http://192.168.1.1/")
passwd = "NmapNetworkScanning"
x = driver.find_elements_by_id('pc-login-password')
for item in x:
    try :
        item.send_keys(passwd)
        item.send_keys(Keys.RETURN)
        break
    except:
        pass

time.sleep(2)

try :
    btn2 = driver.find_element_by_id("confirm-yes").click()
except Exception as e:
    print(e)
    pass

time.sleep(5)

btn_adv = driver.find_element_by_id("advanced").click()
# driver.find_element_by_xpath("//li[@class='ui-menu-item']/").click();
# select_object = Select(btn_adv)

time.sleep(1)

current_used = driver.find_element_by_id("data")
print(current_used)

usage = 0
current_amt = 0
new_ammount = 0

# with open("Current_amount") as F:
#     x = F.readlines()
#     x = x.split["GB"]
#     # "2576.068GB(Monthly Used)"
#     current_amt = x[0]


