import unittest
from selenium import webdriver
import page
import time

class Fullpage_Protected_Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="E:\Selenium Webdriver\chromedriver.exe")
        self.driver.get('http://ymese-interview.local/about/')

    # TEST CASE 1
    def test_Protected_is_activated(self):
        aboutus = page.AboutUsPage(self.driver)
        assert aboutus.is_title_match(), "About us title does't match."
        assert aboutus.is_passster_form_appear(), 'Passter-form is not appear, Page is not protected'
        self.driver.implicitly_wait(10)
        assert not aboutus.is_main_content_appear()
        time.sleep(5)

    # TEST CASE 2
    def test_Valid_Password(self):
        aboutus = page.AboutUsPage(self.driver)
        assert aboutus.is_title_match(), "About us title does't match."
        assert aboutus.is_passster_form_appear(), 'Passter-form is not appear, Page is not protected'
        aboutus.fill_password('YmeseTest')        
        self.driver.implicitly_wait(10)        
        assert not aboutus.is_main_content_appear()
        # time.sleep(5*60)
        # assert not aboutus.is_main_content_appear()
        # time.sleep(15*60)
        # assert not aboutus.is_main_content_appear()
        # time.sleep(30*60)
        # assert not aboutus.is_main_content_appear()
        # time.sleep(60*60)
        # assert not aboutus.is_main_content_appear()
        self.driver.refresh()
        assert aboutus.is_title_match()
        self.driver.implicitly_wait(10)
        assert not aboutus.is_main_content_appear()
        aboutus.submit_password('YmeseTest')        
        self.driver.implicitly_wait(10) 
        assert aboutus.is_main_content_appear()
        time.sleep(5)

    # TEST CASE 3
    def test_Invalid_Password(self):
        aboutus = page.AboutUsPage(self.driver)
        assert aboutus.is_title_match(), "About us title does't match."
        assert aboutus.is_passster_form_appear(), 'Passter-form is not appear, Page is not protected'
        aboutus.submit_password('YmeseTest_wrong')        
        self.driver.implicitly_wait(10)
        assert aboutus.is_alert_appear()
        assert not aboutus.is_main_content_appear()
        # time.sleep(5*60)
        # assert not aboutus.is_main_content_appear()
        # time.sleep(15*60)
        # assert not aboutus.is_main_content_appear()
        # time.sleep(30*60)
        # assert not aboutus.is_main_content_appear()
        # time.sleep(60*60)
        # assert not aboutus.is_main_content_appear()
        self.driver.refresh()
        assert aboutus.is_title_match()
        self.driver.implicitly_wait(10)
        assert not aboutus.is_main_content_appear()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
