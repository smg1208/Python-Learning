from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage
from src.pages.UIObject import UiObject
from src.pages.components.FloatingMenu import FloatingMenu
from src.pages.components.PageFooter import PageFooter
from src.pages.components.PageHeader import PageHeader
from src.utils.Settings import Settings
class HomePage(BasePage):
    GIF = UiObject(By.XPATH, "(//img)[2]")
    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="Advanced Test Runner for Python - Test Junkie",
                          directory="")
        self.header = PageHeader()
        self.footer = PageFooter()
        self.floating_button = FloatingMenu()
    def get_headlines(self):
        """
        :return: DICT, all headlines on the page mapped by the H tag aka
                       {"h1": [...],
                        "h2": [..., ...]}
        """
        headlines = {}
        for heading in ["h1", "h2", "h3"]:
            elements = UiObject(By.TAG_NAME, heading).get_elements()
            for element in elements:
                if heading not in headlines:
                    headlines.update({heading: []})
                headlines[heading].append(UiObject.from_web_element(element).get_text())
        return headlines
    def get_card_info(self):
        """
        :return: LIST of DICTs, Why test junkie cards listed with title, desc, icon, etc aka
                                [{"title": ...,
                                  "description": ...,
                                 {...},
                                 {...}]
        """
        cards = []
        card = "//div[@class = 'card-content']"
        for index in range(1, 5):
            cards.append({"title": UiObject(By.XPATH, "({}/span)[{}]".format(card, index)).get_text(),
                          "description": UiObject(By.XPATH, "({}/p)[{}]".format(card, index)).get_text()})
        return cards
    def get_quote(self):
        """
        :return: DICT, structured data for the currently active quote that is on the screen aka
                       {"name": ..., "quote": ..., "title": ...}
        """
        block = "//div[contains(@class, 'slick-slide slick-current')]"
        return {"name": UiObject(By.XPATH, "{}//h3".format(block)).get_text(),
                "quote": UiObject(By.XPATH, "{}//blockquote".format(block)).get_text(),
                "title": UiObject(By.XPATH, "{}//p".format(block)).get_text()}