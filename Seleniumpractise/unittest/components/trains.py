class Trains:
    def verifyTrainsPage(self,driver):
        res=driver.find_element_by_xpath("//h1[contains(text(),'Search trains')]").is_displayed()
        if res:
            print("i am into trains page of app")
        else:
            print("i am not into trains page")
