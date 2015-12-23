import unittest
from selenium import webdriver

class Navigation1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # get the path of the ChromeDriver
        chrome_driver_path = "C:/Users/DwightNorris/Documents/Programming/Selenium-Webdriver/Python/chromedriver.exe"

        # create a new Firefox session
        cls.driver = webdriver.Chrome(chrome_driver_path)
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

        # navigate to the application home page
        cls.driver.get('http://www.dwightbnorris.com/')

    def test_a_about_page(self):
        # use about me link
        about_button = self.driver.find_element_by_partial_link_text("About")
        about_button.click()
        self.driver.implicitly_wait(5)

    def test_b_contact_page(self):
        # use about me link
        contact_button = self.driver.find_element_by_partial_link_text("Contact")
        contact_button.click()
        self.driver.implicitly_wait(5)

    def test_c_blog_page(self):
        # use about me link
        blog_button = self.driver.find_element_by_partial_link_text("Blog")
        blog_button.click()
        self.driver.implicitly_wait(5)

    def test_d_resume_page(self):
        # use about me link
        resume_button = self.driver.find_element_by_partial_link_text("Resume")
        resume_button.click()
        self.driver.implicitly_wait(5)

    def test_e_projects_page(self):
        # use about me link
        projects_button = self.driver.find_element_by_partial_link_text("Projects")
        projects_button.click()
        self.driver.implicitly_wait(5)

    def test_f_certifications_page(self):
        # use about me link
        certifications_button = self.driver.find_element_by_partial_link_text("Certifications")
        certifications_button.click()
        self.driver.implicitly_wait(5)

    def test_g_home_page(self):
        # use about me link
        home_button = self.driver.find_element_by_partial_link_text("Home")
        home_button.click()
        self.driver.implicitly_wait(5)

    def test_h_github_button(self):
        # test github button
        github_button = self.driver.find_element_by_class_name('fa-github')
        github_button.click()
        self.driver.implicitly_wait(5)
        self.driver.get('http://www.dwightbnorris.com/')
        self.driver.implicitly_wait(5)

    def test_i_github_gist_button(self):
        # test github gist button
        github_gist_button = self.driver.find_element_by_class_name('fa-github-alt')
        github_gist_button.click()
        self.driver.implicitly_wait(5)
        self.driver.get('http://www.dwightbnorris.com/')
        self.driver.implicitly_wait(5)

    def test_j_linkedin_button(self):
        linkedin_button = self.driver.find_element_by_class_name('fa-linkedin-square')
        linkedin_button.click()
        self.driver.implicitly_wait(5)
        self.driver.get('http://www.dwightbnorris.com/')
        self.driver.implicitly_wait(5)

    def test_k_twitter_button(self):
        twitter_button = self.driver.find_element_by_class_name('fa-twitter')
        twitter_button.click()
        self.driver.implicitly_wait(5)
        self.driver.get('http://www.dwightbnorris.com/')
        self.driver.implicitly_wait(5)

    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)