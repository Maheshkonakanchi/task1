from selenium import webdriver
from selenium.webdriver.common.action_chains import *

import time
driver=webdriver.Chrome(executable_path="D:\\software\\selenium drivers\\chromedriver.exe")
driver.get("https://www.gmail.com")
username=driver.find_element_by_xpath("//*[@type='email']")
username.send_keys("panterra.mounika")
time.sleep(5)
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
time.sleep(10)
password=driver.find_element_by_xpath("//*[@type='password']")
password.send_keys("qa@12345")
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()
driver.maximize_window()
time.sleep(10)
search=driver.find_element_by_xpath("//*[@class='gb_df']")
search.send_keys("ACD SLA")
time.sleep(3)
driver.find_element_by_xpath("//*[@id='aso_search_form_anchor']/button[4]").click()

print("Search donne")
time.sleep(30)
print(driver.find_element_by_xpath("//div[@tabindex='0'][@data-tooltip='Select']").get_attribute("id"))
#driver.find_element_by_xpath("//div[@class='J-J5-Ji J-JN-M-I-Jm']//div[@class='G-asx T-I-J3 J-J5-Ji']").click()

driver.find_element_by_xpath("//*[@id=':15n']").click()
driver.find_element_by_xpath("//*[@id=':26q']/div/div").click()
driver.find_element_by_xpath("class='J-JK-Jz'").click()

time.sleep(10)
#driver.find_element_by_xpath("//*[@id='gb']/div[2]/div[3]/div/div[2]/div/a/span").click()
#driver.find_element_by_xpath("//*[@id='gb_71']").click()