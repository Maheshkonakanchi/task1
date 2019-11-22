from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
driver=webdriver.Chrome("D:\\software\\selenium drivers\\chromedriver.exe")
driver.get("https://www.cleartrip.com")
driver.maximize_window()
time.sleep(15)

from_place=driver.find_element_by_xpath("//input[@id='FromTag']")
from_place.send_keys("Hyderabad")
to_place=driver.find_element_by_xpath("//input[@id='ToTag']")
to_place.send_keys("Delhi")
driver.find_element_by_xpath("//input[@id='DepartDate']").click()
#driver.switch_to_alert().accept()
month=driver.find_element_by_xpath("//span[contains(text(),'October')]")
print(month.text)
if month.text=='November':
    driver.find_element_by_xpath("//dl[@class='vertical']//i[@class='icon ir datePicker'][contains(text(),'Cal')]").click()
    date_picker=driver.find_element_by_xpath("//div[contains(@class,'monthBlock first')]//a[contains(@class,'ui-state-default')][contains(text(),'25')]").click()
else:
    driver.find_element_by_xpath("//a[contains(@class,'nextMonth')]").click()
    date_picker=driver.find_element_by_xpath("//div[contains(@class,'monthBlock first')]//a[contains(@class,'ui-state-default')][contains(text(),'25')]").click()

a=Select(driver.find_element_by_xpath("//select[@id='Adults']"))
a.select_by_visible_text("5")
b=Select(driver.find_element_by_xpath("//select[@id='Childrens']"))
b.select_by_value("2")
c=Select(driver.find_element_by_xpath("//select[@id='Infants']"))
c.select_by_index("0")
driver.find_element_by_xpath("//input[@id='SearchBtn']").click()
time.sleep(15)
flight_name=[]
flight_name=driver.find_elements_by_xpath("//li[@class='listItem  nonBundled  ']//img")
flight_name.get_attribute("title")
for x in flight_name:
    print(x)

#driver.close()