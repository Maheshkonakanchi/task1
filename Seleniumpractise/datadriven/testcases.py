import XLutiles
from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C://Users//Mahesh//PycharmProjects//streamsbeta//drivers//chromedriver.exe")
url="https://gostreams.beta-wspbx.com"
driver.maximize_window()
driver.get(url)

path="C://Users//Mahesh//Desktop//streamsusers.xlsx"
rows=XLutiles.getrowcount(path,'Sheet1')
cols=XLutiles.getcolumncount(path,"Sheet1")
print("Total number of rows present in sheet :" + str(rows))
print("Total number of columns present in sheet :"+ str(cols))

for r in range(2,rows+1):
     username=XLutiles.readData(path,"Sheet1",r,1)
     password=XLutiles.readData(path,"Sheet1",r,2)
     print(username)
     print(password)
     driver.find_element_by_xpath("//input[@id='xusername']").send_keys(username)
     driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
     driver.find_element_by_xpath("//input[@id='login_button']").click()
     time.sleep(15)
     print(driver.title)
     if driver.current_url=="https://gostreams.beta-wspbx.com/sloader/home.jsp":
       print("Pass")
       XLutiles.writeData(path,"Sheet1",r,3,"Pass")
       driver.find_element_by_xpath("//a[@id='streams_menu_icon_area']").click()
       driver.find_element_by_xpath("//li[contains(text(),'Logout')]").click()
       time.sleep(15)
       print("**************************")
     else:
       print("Fail")
       XLutiles.writeData(path,"Sheet1",r,3,"fail")
       time.sleep(10)
       driver.get(url)


driver.close()