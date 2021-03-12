from element import BasePageElement
from locators import AboutUsPageLocators


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class AboutUsPage(BasePage):

    def is_title_match(self):
        return "About us" in self.driver.title

    def is_passster_form_appear(self):
        try:
            self.driver.find_element(*AboutUsPageLocators.PASSSTER_FORM)
            return True
        except Exception:
            return False

    def is_main_content_appear(self):
        try:
            self.driver.find_element(*AboutUsPageLocators.MAIN_CONTENT)
            return True
        except Exception:
            return False

    def is_alert_appear(self):
        try:
            self.driver.find_element(*AboutUsPageLocators.PASSSTER_ERROR)
            return True
        except Exception:
            return False

    def fill_password(self, password):
        box = self.driver.find_element(
            *AboutUsPageLocators.PASSSTER_PASSWORD_INPUT)
        box.send_keys(password)

    def submit_password(self, password):
        box = self.driver.find_element(
            *AboutUsPageLocators.PASSSTER_PASSWORD_INPUT)
        box.send_keys(password)
        submit = self.driver.find_element(*AboutUsPageLocators.PASSSTER_SUBMIT)
        submit.click()
