import unittest
from selenium import webdriver
import page

class PythonSearch(unittest.TestCase):
    def setUp(self):
        print('set it up')
        self.driver = webdriver.Chrome('E:\Selenium Webdriver\chromedriver.exe')
        self.driver.get('https://www.python.org')

    # Test case alway start with test
    def test_search_python(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matchs()
        mainPage.search_text_element = 'pycon'        
        mainPage.click_go_button()
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.is_result_found()

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matchs()

    def test_search_2(self):
        print('test')
        assert True

    def aha_test_search(self):
        print('this wont print!')

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()