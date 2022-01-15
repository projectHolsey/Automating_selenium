from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import time

driver = webdriver.Chrome('./chromedriver_win32/chromedriver')
driver.get("https://www.youtube.com/watch?v=GGXzlRoNtHU&ab_channel=KOCHRECORDS")

x = driver.find_elements_by_class_name('VfPpkd-dgl2Hf-ppHlrf-sM5MNb')

for i, item in enumerate(x):
    if i < 5:
        continue
    item.click()

    strt = time.time()
    while time.time() - strt < 16:
        try :
            time.sleep(8)
            button = driver.find_element_by_class_name('ytp-ad-skip-button-container')
            button.click()
        except Exception as e:
            pass
    break

time.sleep(17)

driver.close()