class HomePage:
    def verifyHomePage(self,driver):
        res=driver.find_element_by_xpath("//h1[contains(text(),'Search flights')]").is_displayed()
        if res:
            print("i am into home page of app")
        else:
            print("i am not into home page")
            
    def navigateToTrainsPage(self,driver):
        driver.find_element_by_xpath("//a[contains(text(),'Trains')]").click()
    
