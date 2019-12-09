import time

from utils import xlutils

file = "C:\\Users\\Mahesh.K\\PycharmProjects\\git hub projects\\StreamsBeta\\inputfiles\\userdetails.xlsx"
sheetname="users_sheet"

class userinfo:

    def getuserdetails(self,driver):
        #XLutils.getrowcount(file,sheetname)
        #driver.close()
        rows = xlutils.getrowcount(file ,sheetname)
        #colu = xlutils.getcolumncount(file, sheetname)

        for r in range(2, rows + 1):
            username = xlutils.readdata(file, sheetname, r, 2)
            password = xlutils.readdata(file, sheetname, r, 3)
            print(username)
            print(password)
            driver.find_element_by_xpath("//input[@id='xusername']").send_keys(username)
            driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
            driver.find_element_by_xpath("//input[@id='login_button']").click()
            time.sleep(15)
            print(driver.title)
            if driver.current_url == "https://gostreams.beta-wspbx.com/sloader/home.jsp":
                print("Pass")
                xlutils.writedata(file, sheetname, r, 5, "Pass")
                driver.find_element_by_xpath("//a[@id='streams_menu_icon_area']").click()
                driver.find_element_by_xpath("//li[contains(text(),'Logout')]").click()
                time.sleep(15)
                print("**************************")
            else:
                print("Fail")
                xlutils.writedata(file, sheetname, r, 5, "fail")
                time.sleep(10)
                driver.get("https://gostreams.beta-wspbx.com/")
                print("**************************")
