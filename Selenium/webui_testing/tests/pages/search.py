from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class PythonSearch:
    url = 'https://www.python.org'

    SEARCH_INPUT = (By.NAME,'q')

    def __init__(self,browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.url)
    
    def search(self,phrase):
        search_input= self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)