from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome("D:\\software\\selenium drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.cleartrip.com")
driver.implicitly_wait(20)
driver.find_element_by_xpath("//a[contains(text(),'Trains')]").click()
driver.find_element_by_xpath("//h1[contains(text(),'Search trains')]").is_displayed()
driver.find_element_by_xpath("//input[@id='from_station']").send_keys("Secunderabad Junction (SC)")
driver.find_element_by_xpath("//input[@id='to_station']").send_keys("Delhi (DLI)")
time.sleep(10)
a=Select(driver.find_element_by_xpath("//select[@id='trainClass']"))
time.sleep(2)
a.select_by_value("1A")
driver.find_element_by_xpath("//button[@id='trainFormButton']").click()
driver.find_element_by_xpath("//a[@class='cal_openLink']//img").click()
driver.find_element_by_xpath("(//td[@class='weekend']//a[contains(text(),'30')])[1]").click()
b=Select(driver.find_element_by_xpath("//select[@id='train_adults']"))
b.select_by_value("2")
driver.find_element_by_xpath("//button[@id='trainFormButton']").click()

