import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class login:

    def loginuser(self, driver, username_path, password_path, loginbutton_path, username, password):
        driver.find_element_by_xpath(username_path).send_keys(username)
        driver.find_element_by_xpath(password_path).send_keys(password)
        driver.find_element_by_xpath(loginbutton_path).click()
        time.sleep(10)
        print("Logined sucessfully")

    def checkstatus(self, driver):
        WebDriverWait(driver, 30).until(
            ec.text_to_be_present_in_element((By.XPATH, "//div[@id='status_msg']"), "On Desktop"))
        status = driver.find_element_by_xpath("//*[@id='status_msg']")
        print("status of user is :" + status.text)
