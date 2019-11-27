import subprocess
import unittest
from utils import browserutils
from stepstodo import loginofuser
from  stepstodo import searchforuser
from  stepstodo import uploaddata


class TestSuitestreams(unittest.TestCase):
    def testscript(self):
        driver=browserutils.Browser().openBrowser()
        loginofuser.login().loginuser(driver)
        loginofuser.login().checkstatus(driver)
        searchforuser.streamuser().searchauser(driver)
        uploaddata.Upload().uploaddata(driver)

subprocess._cleanup()

if __name__ == "__main__":
    unittest.main()



