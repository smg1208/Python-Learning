from locator import *
from element import BasePageElement


class SearchTextElement(BasePageElement):
    locator = 'q'
# class GoButtonElement(BasePageElement):
#     locator = 'go'


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matchs(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        ele = self.driver.find_element(*MainPageLocators.go_Button)
        ele.click()


class SearchResultPage(BasePage):
    def is_result_found(self):
        return 'No results found.' not in self.driver.page_source
