from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="D:\\software\\selenium drivers\\chromedriver.exe")
driver.get("https://test1.absofttrainings.com/javascript-alert-confirm-prompt-boxes/")
time.sleep(10)
driver.find_element_by_xpath("//*[@onclick='alertBox()']").click()
time.sleep(5)
driver.switch_to.alert.accept()
driver.get_screenshot_as_file("C:\\Users\\Mahesh.K\\PycharmProjects\\Seleniumpractise\\screeenshots\\text.1.png")
