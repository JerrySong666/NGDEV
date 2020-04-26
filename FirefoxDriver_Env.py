#coding: UTF-8
from selenium import webdriver
from time import sleep
# https://github.com/mozilla/geckodriver
driver=webdriver.Firefox()
url='http://www.baidu.com'
driver.get(url)
driver.maximize_window()
sleep(5)
driver.find_element_by_id('kw').send_keys("python")
driver.find_element_by_id('su').click()
sleep(5)
driver.quit()