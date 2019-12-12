import subprocess
import unittest

from utils import browserutils
from stepstodo import loaduserdata
from stepstodo import Createfolder

class TestSuitestreams(unittest.TestCase):

    def testscript(self):
        driver = browserutils.Browser().openBrowser()
        loaduserdata.userinfo().getuserdetails(driver)
        Createfolder.folder().testcasetwo(driver)



subprocess._cleanup()

if __name__ == "__main__":
    unittest.main()
