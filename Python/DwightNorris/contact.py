import unittest
from selenium import webdriver

class Contact(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('http://www.dwightbnorris.com/contact.php')

    def test_a_name(self):
        # email form - name
        name = self.driver.find_element_by_name('name1')
        name.send_keys('Dwight Norris')
        self.driver.implicitly_wait(5)

    def test_b_email(self):
        email = self.driver.find_element_by_id('email1')
        email.send_keys('norrisdb@yahoo.com')

    def test_c_message(self):
        message = self.driver.find_element_by_name('message1')
        message.send_keys('This is a test!')

    def test_d_security(self):
        security = self.driver.find_element_by_id('human1')
        security.send_keys('11')

    def test_e_submit(self):
        submit1 = self.driver.find_element_by_id('submit1')
        submit1.click()
        self.driver.implicitly_wait(15)

    def test_f_name(self):
        # email form - name
        name = self.driver.find_element_by_name('name')
        name.send_keys('Dwight Norris')

    def test_g_email(self):
        email = self.driver.find_element_by_id('email')
        email.send_keys('norrisdb@yahoo.com')

    def test_h_message(self):
        message = self.driver.find_element_by_name('message')
        message.send_keys('This is a test!')

    def test_i_security(self):
        security = self.driver.find_element_by_id('human')
        security.send_keys('11')

    def test_j_submit(self):
        submit2 = self.driver.find_element_by_id('submit2')
        submit2.click()
        self.driver.implicitly_wait(15)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)