import time


class Upload:
    def uploaddata(self, driver):
        driver.find_element_by_xpath("//*[@placeholder='Type your message here']").send_keys("its a test message")
        print("text message sent")
        time.sleep(10)
