from selenium import webdriver

class Browser:
    def openBrowser(self):
        self.driver=webdriver.Chrome(executable_path="C:\\Users\\ADMIN\\p1\\AAA\\drivers\\chromedriver.exe")
        self.driver.get("https://www.google.com")
        self.driver.maximize_window()
        return self.driver
        #time.sleep(3)
               
    def  invokeApp(self,driver):
        driver.get("https://www.cleartrip.com/")
        
    def  closeBrowser(self,driver):
        driver.quit()