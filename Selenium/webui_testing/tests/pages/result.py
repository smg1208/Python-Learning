from selenium.webdriver.common.by import By

class PythonSearchResult:
    search_input =(By.NAME,'q')
    
    @classmethod
    def PHRASE_RESULT(cls):
        xpath = "//ul[@class='list-recent-events menu']/li"
        return (By.XPATH,xpath)
    
    def __init__(self,browser):
        self.browser = browser

    def phrase_result_count(self):
        phrase_results = self.browser.find_elements(*self.PHRASE_RESULT())
        print(phrase_results)
        print(len(phrase_results))        
        return len(phrase_results)

    def search_input_value(self):
        search_input = self.browser.find_element(*self.search_input)
        return search_input.get_attribute('value')
    
