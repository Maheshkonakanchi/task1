import time


class streamuser:
    def searchauser(self, driver):
        driver.find_element_by_xpath("//input[@id='search_recents']").send_keys("kmaheshtwo@security")
        driver.find_element_by_xpath(
            "//span[@id='buddy_display_name_8134155c8ad411e6b48f001e58a7db4a_3_kmaheshtwo@security']//span[contains(@class,'suid')][contains(text(),'kmaheshtwo@security')]").click()
        time.sleep(10)
        print("search completed")
