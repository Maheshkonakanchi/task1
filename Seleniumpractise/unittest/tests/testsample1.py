import unittest
from utils import browserutils
from components import homepage
from components import trains

class TestSuite1(unittest.TestCase):

    def testm1(self):     
        driver = browserutils.Browser().openBrowser()   
        browserutils.Browser().invokeApp(driver)
        homepage.HomePage().verifyHomePage(driver)
        homepage.HomePage().navigateToTrainsPage(driver)
        trains.Trains().verifyTrainsPage(driver)
        browserutils.Browser().closeBrowser(driver)


if __name__ == "__main__":
    unittest.main()
