from selenium import webdriver
from selenium.webdriver.support import *
import time

driver=webdriver.Chrome(executable_path="D:\\software\\selenium drivers\\chromedriver.exe")
driver.get("https://test1.absofttrainings.com/javascript-alert-confirm-prompt-boxes/")
driver.implicitly_wait(20)

driver.find_element_by_xpath("//*[@onclick='confirmBox()']").click()
time.sleep(5)

driver.switch_to.alert.dismiss()
time.sleep(5)

driver.close()


