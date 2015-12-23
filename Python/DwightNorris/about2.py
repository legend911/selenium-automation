import unittest
from selenium import webdriver

class About2(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # get the path of the IEDriverServer
        ie_driver_path = "C:/Users/DwightNorris/Documents/Programming/Selenium-Webdriver/Python/IEDriverServer.exe"

        # create a new Firefox session
        cls.driver = webdriver.Ie(ie_driver_path)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('http://www.dwightbnorris.com/about.html')

    def test_a_about_page(self):
        # test about page collapse window (journey)
        journey = self.driver.find_element_by_partial_link_text('Journey')
        journey.click()

    def test_b_about_page(self):
        # test about page collapse window (goals)
        goals = self.driver.find_element_by_partial_link_text('Goals')
        goals.click()

    def test_c_about_page(self):
        # test about page collapse window (progress)
        progress = self.driver.find_element_by_partial_link_text('Progress')
        progress.click()

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)