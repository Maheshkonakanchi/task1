from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="D:\\software\\selenium drivers\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.spicejet.com/")
time.sleep(10)
driver.find_element_by_xpath("//*[contains(text(),'Group Travel')]").click()
time.sleep(5)
print("Clicked on Group Travel")
print(driver.window_handles)
time.sleep(5)
driver.find_element_by_xpath("//*[contains(text(),'Cargo')]").click()
print("Clicked on Cargo")
print(driver.window_handles)
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(),'SME Travel')]").click()
print("Clicked on SME travel")
print(driver.window_handles)
time.sleep(5)
driver.find_element_by_xpath("//span[contains(text(),'GST Invoice')]").click()
print("Clicked on GST Invoice")
print(driver.window_handles)
print(len(driver.window_handles))
time.sleep(15)

driver.find_element_by_xpath("//span[contains(text(),'Corporate Traveller')]").click()
print("Clicked on Corporate Traveller")
print(driver.window_handles)
time.sleep(15)

driver.find_element_by_xpath("//span[contains(text(),'Visa Services')]").click()
print("Clicked on Visa service")
print(driver.window_handles)




driver.get_screenshot_as_file("C:\\Users\\Mahesh.K\\PycharmProjects\\Seleniumpractise\\screeenshots\\text.1.png")
