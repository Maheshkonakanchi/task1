from selenium import webdriver
from selenium.webdriver.support import *
import time

driver=webdriver.Chrome(executable_path="D:\\software\\selenium drivers\\chromedriver.exe")
driver.get("https://test1.absofttrainings.com/javascript-alert-confirm-prompt-boxes/")
driver.implicitly_wait(20)
driver.find_element_by_xpath("//*[@id='prompt']").click()
time.sleep(5)
obj=driver.switch_to.alert
obj.send_keys("Mahesh")
time.sleep(5)
obj.accept()
time.sleep(5)
textentered=driver.find_element_by_xpath("//*[@id='msg']")


print(textentered.text)
driver.close()



