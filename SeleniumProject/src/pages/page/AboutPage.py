from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage
from src.pages.UIObject import UiObject
from src.pages.components.FlashMsg import FlashMsg
from src.pages.components.FloatingMenu import FloatingMenu
from src.pages.components.PageFooter import PageFooter
from src.pages.components.PageHeader import PageHeader
from src.utils.Settings import Settings
class AboutPage(BasePage):
    AUTHOR_IMG = UiObject(By.XPATH, "//img[@class='team_member']")
    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="About - Test Junkie",
                          directory="/about/")
        self.header = PageHeader()
        self.footer = PageFooter()
        self.floating_button = FloatingMenu()
        self.flash_msg = FlashMsg()
    def get_description(self):
        return UiObject(By.XPATH, "//div[@id = 'content']/p").get_text()
    def get_project_status_links(self):
        links = []
        elements = UiObject(By.XPATH, "//div[@id = 'project_status']/a").get_elements()
        for element in elements:
            links.append(UiObject.from_web_element(element))
        return links