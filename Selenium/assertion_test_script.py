import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from database_selenium import dbsele as db
import time


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        # Create new Chrome session
        cls.driver = webdriver.Chrome(executable_path=db.wd_path.get('chrome'))
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # Navigate to website homepage
        cls.driver.get('https://www.google.com')

    def is_element_present(self, byLocator, element):
        try:
            self.driver.find_element(by=byLocator, value=element)
        except NoSuchElementException:
            return False
        return True

    def test_search_box(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_setting(self):
        self.assertTrue(self.is_element_present(By.ID, 'SIvCob'))

    def test_image_link(self):
        image_link = self.driver.find_element(
            by=By.CSS_SELECTOR, value="a[class='gb_g'][data-pid='2']")
        image_link.click()
        # check search field exists on Images page
        self.assertTrue(self.is_element_present(By.NAME, "q"))
        search_field = self.driver.find_element_by_name('q')
        search_field.send_keys('slenium locator icon')
        search_field.submit()
        time.sleep(5)

    @classmethod
    def tearDown(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
