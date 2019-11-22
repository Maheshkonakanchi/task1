from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome("D:\\software\\selenium drivers\\chromedriver.exe")
driver.get("https://www.cleartrip.com")
driver.maximize_window()
time.sleep(5)
onetrip=driver.find_element_by_xpath("//input[@id='OneWay']").is_selected()

if onetrip:
    print("Already selected")
else:
    print("by default not selected")
roundtrip=driver.find_element_by_xpath("//input[@id='RoundTrip']").is_selected()

"""if roundtrip:
    print("roundtrip is selected")
else:
    driver.find_element_by_xpath("//input[@id='RoundTrip']").click()
    print("Roundtrip is selected")"""
from_place=driver.find_element_by_xpath("//input[@id='FromTag']")
from_place.send_keys("Hyderabad")
to_place=driver.find_element_by_xpath("//input[@id='ToTag']")
to_place.send_keys("Delhi")
driver.find_element_by_xpath("//input[@id='DepartDate']").click()
time.sleep(0)
month=driver.find_element_by_xpath("//span[contains(text(),'October')]")
print(month.text)
if month.text=='November':
    driver.find_element_by_xpath("//dl[@class='vertical']//i[@class='icon ir datePicker'][contains(text(),'Cal')]").click()
    date_picker=driver.find_element_by_xpath("//div[contains(@class,'monthBlock first')]//a[contains(@class,'ui-state-default')][contains(text(),'25')]").click()
else:
    driver.find_element_by_xpath("//a[contains(@class,'nextMonth')]").click()
    date_picker=driver.find_element_by_xpath("//div[contains(@class,'monthBlock first')]//a[contains(@class,'ui-state-default')][contains(text(),'25')]").click()
"""driver.find_element_by_xpath("//input[@id='ReturnDate']").click()
driver.find_element_by_xpath("//a[contains(@class,'nextMonth')]")
monthtwo=driver.find_element_by_xpath("//span[contains(text(),'November')]")
driver.find_element_by_xpath("//div[contains(@class,'monthBlock last')]//a[contains(@class,'ui-state-default')][contains(text(),'26')]").click()
print(monthtwo.text)"""
a=Select(driver.find_element_by_xpath("//select[@id='Adults']"))
a.select_by_visible_text("5")
b=Select(driver.find_element_by_xpath("//select[@id='Childrens']"))
b.select_by_value("2")
c=Select(driver.find_element_by_xpath("//select[@id='Infants']"))
c.select_by_index("0")
driver.find_element_by_xpath("//input[@id='SearchBtn']").click()
time.sleep(15)
"""depature=driver.find_element_by_xpath("(//*[@class='depart'])[position()=4]")
print(depature.text)"""
driver.find_element_by_xpath("//a[@class='current sortAsc']").click()
ticketcost=driver.find_element_by_xpath("(//*[@class='price'])[position()=2]")
print("Heighest price of the flight =" +ticketcost.text)
flightname=driver.find_element_by_xpath("(//*[@class='vendor  count1 '])[position()=1]")
print("flight name ="+flightname.text)

thirdflight=driver.find_element_by_xpath("(//*[@class='depart'])[position()=4]")
print("third flight depart time =" +thirdflight.text)

