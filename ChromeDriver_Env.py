#coding: UTF-8
from selenium import webdriver
from time import sleep
# 下载地址
# http://chromedriver.storage.googleapis.com/index.html
driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("刘德华")
driver.find_element_by_id("su").click()



sleep(5)
driver.quit()



