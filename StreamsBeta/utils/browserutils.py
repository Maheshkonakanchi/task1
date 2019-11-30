from selenium import webdriver


class Browser:
    def openBrowser(self):
        self.driver = webdriver.Chrome(executable_path="D:\\software\\selenium drivers\\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.get("https://gostreams.beta-wspbx.com/")
        return self.driver


"""
    def openothertab(self,driver):
        self.driver.find_element_by_xpath("//header[@class='streamsHeader']").send_keys(Keys.control,"t")

"""
