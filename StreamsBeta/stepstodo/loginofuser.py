from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time
class login:
    def loginuser(self,driver):
        driver.find_element_by_xpath("//input[@id='xusername']").send_keys("kmaheshone@security")
        driver.find_element_by_xpath("//input[@id='password']").send_keys("abc@1234")
        driver.find_element_by_xpath("//input[@id='login_button']").click()
        time.sleep(10)
        print("Logined sucessfully")
    def checkstatus(self,driver):
        WebDriverWait(driver,30).until(ec.text_to_be_present_in_element((By.XPATH,"//div[@id='status_msg']"),"On Desktop"))
        status=driver.find_element_by_xpath("//*[@id='status_msg']")
        print("status of user is :"+ status.text )