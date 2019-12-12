from utils import xlutils
file = "C:\\Users\\Mahesh.K\\PycharmProjects\\git hub projects\\StreamsBeta\\inputfiles\\userdetails.xlsx"
sheetname="drivefolders"
class folder:
    def testcasetwo(self,driver):
        rows=xlutils.getrowcount(file,sheetname)
        colm=xlutils.getcolumncount(file,sheetname)
        rows = xlutils.getrowcount(file, sheetname)
        # colu = xlutils.getcolumncount(file, sheetname)

        for r in range(2, rows + 1):
            username = xlutils.readdata(file, sheetname, r, 6)
            password = xlutils.readdata(file, sheetname, r, 7)
            print(username)
            print(password)
            driver.find_element_by_xpath("//input[@id='xusername']").send_keys(username)
            driver.find_element_by_xpath("//input[@id='password']").send_keys(password)
            driver.find_element_by_xpath("//input[@id='login_button']").click()
            time.sleep(15)
            driver.find_element_by_xpath("//a[@id='spaneltabanc_3']").click()
            for n in range(2,rows + 1):
                filename=xlutils.readdata(file, sheetname, r, 2)
                print(filename)
                driver.find_element_by_xpath("//div[@id='webdrive_icons_panel_opicons']")
                driver.find_element_by_xpath("//input[@id='webdrive_createfolder']").sendkeys(filename)
                driver.find_element_by_xpath("//div[@id='displayFolder']//form//div//input[@class='normalButton']").click()
                if
