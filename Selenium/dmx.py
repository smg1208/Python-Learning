import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from database_selenium import dbsele as db
import time


class DMXTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path=db.wd_path.get('chrome'))
    
    def test_search_in_python_org(self):
        driver = self.driver
        action = ActionChains(driver)
        driver.get('https://www.dienmayxanh.com')
        self.assertIn("Siêu thị Điện máy", driver.title)
        el = driver.find_element_by_css_selector("li[data-submenu-id='submenu-7']")
        action.move_to_element(el).perform()        
        el2 = driver.find_element_by_css_selector("a[href='/may-doi-tra/tu-lanh']")
        el2.click()
        
        assert "No results found." not in driver.page_source
        time.sleep(15)   
    
    
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()       
