import subprocess
import unittest

from stepstodo import loaduserdata
from stepstodo import loginofuser
from stepstodo import searchforuser
from stepstodo import uploaddata
from utils import browserutils


class TestSuitestreams(unittest.TestCase):

    def testscript(self):
        driver = browserutils.Browser().openBrowser()
        loaduserdata.getuserdetails().getuserinfo()
        loginofuser.login().loginuser(driver)
        loginofuser.login().checkstatus(driver)
        searchforuser.streamuser().searchauser(driver)
        uploaddata.Upload().uploaddata(driver)


subprocess._cleanup()

if __name__ == "__main__":
    unittest.main()
