import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import database_selenium as db
import time


class PythonOrgSearch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):        
        cls.driver = webdriver.Chrome(executable_path=db.wd_path.get('chrome'))
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://www.google.com/")
        cls.driver.title
    
    def test_search_by_text(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys("python tutorials")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        lists = self.driver.find_elements_by_class_name("r")
        for i in lists:
            childtitle = i.find_element_by_css_selector("h3[class='LC20lb DKV0Md']")
            print(childtitle.text)
        time.sleep(30)
    
    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_name("q")
        # enter search keyword and submit
        self.search_field.send_keys("Python class")
        self.search_field.submit()
        #get the list of elements which are displayed after the search
        #currently on result page using find_elements_by_class_name method
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(11, len(list_new))
    
    @classmethod
    def tearDownClass(cls):        
        cls.driver.close()

if __name__ == "__main__":
    unittest.main()       
