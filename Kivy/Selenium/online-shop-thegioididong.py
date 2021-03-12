import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException


class CreatingGoogleAccount(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            executable_path="C:\Program Files (x86)\Google\Chrome\chromedriver.exe")

    def testCreatingAccountbyPythonSelenium(self):
        driver = self.driver
        driver.get("https://myaccount.google.com/intro")
        self.assertIn("Account", driver.title)
        elem = driver.find_element_by_link_text("Create a Google Account")
        elem.send_keys(Keys.ENTER)
        self.assertIn("Create", driver.title)
        print()
        print(' Account information! '.center(60, '-'))
        elem = driver.find_element_by_name("firstName")
        elem.send_keys("Tuấn Anh")
        elem = driver.find_element_by_name("lastName")
        elem.send_keys("Lê")
        elem = driver.find_element_by_name("Username")
        elem.send_keys("anh.letuan3.gg.dn")
        elem = driver.find_element_by_name("Passwd")
        elem.send_keys("Vtpl191681234")
        elem = driver.find_element_by_name("ConfirmPasswd")
        print('elem - cf pass: ', elem)
        elem.send_keys("Vtpl191681234")
        elem = driver.find_element_by_id("accountDetailsNext")
        elem.send_keys(Keys.ENTER)
        time.sleep(5)

        print()
        print(' Input phone number '.center(60, '-'))
        number = input('Your phone number to received active code: ')
        elem = driver.find_element_by_id("phoneNumberId")
        elem.send_keys(number)
        elem = driver.find_element_by_id("gradsIdvPhoneNext")
        elem.send_keys(Keys.ENTER)
        time.sleep(5)

        print()
        print(' Code '.center(60, '-'))
        number = input('Your received active code: ')
        elem = driver.find_element_by_id("code")
        elem.send_keys(number)
        elem = driver.find_element_by_id("gradsIdvVerifyNext")
        elem.send_keys(Keys.ENTER)
        time.sleep(5)
        while True:
            try:
                verify = driver.find_element_by_id('code')
                print()
                print(' Code Invalid '.center(60, '-'))
                number = input('Re-input your received active code: ')
                verify.clear()
                verify.send_keys(number)
                elem = driver.find_element_by_id("gradsIdvVerifyNext")
                elem.send_keys(Keys.ENTER)
                time.sleep(15)
            except NoSuchElementException:
                break

        print()
        print(' Account Profile! '.center(60, '-'))
        elem = driver.find_element_by_link_text(
            'Recovery email address (optional)')
        elem.send_keys("anh.letuan3.icloud@gmail.com")
        time.sleep(1500)
        elem = driver.find_element_by_name("lastName")
        elem.send_keys("Lê")
        elem = driver.find_element_by_name("Username")
        elem.send_keys("anh.letuan3.gg.dn")
        elem = driver.find_element_by_name("Passwd")
        elem.send_keys("Vtpl191681234")
        elem = driver.find_element_by_name("ConfirmPasswd")
        print('elem - cf pass: ', elem)
        elem.send_keys("Vtpl191681234")
        elem = driver.find_element_by_id("accountDetailsNext")
        elem.send_keys(Keys.ENTER)
        time.sleep(15)

    def tearDown(self):
        print('here')
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
