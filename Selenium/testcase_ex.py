import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import database as db
import time


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=db.wd_path.get('chrome'))
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('https://www.python.org')
        self.assertIn("Python", driver.title)
        el = driver.find_element_by_name('q')
        el.clear()
        el.send_keys('pycon')
        el.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        time.sleep(15)
    
    def test_to_do_other_search(self):     
        driver = self.driver   
        driver.get('https://www.google.com')
        self.assertIn("Google", driver.title)
        el = driver.find_element_by_name('q')
        el.clear()
        el.send_keys('python.org')
        el.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source
        time.sleep(15)
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()       
