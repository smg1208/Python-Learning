from selenium.webdriver.common.by import By
from src.pages.BasePage import BasePage
from src.pages.UIObject import UiObject
from src.pages.components.FlashMsg import FlashMsg
from src.pages.components.FloatingMenu import FloatingMenu
from src.pages.components.PageFooter import PageFooter
from src.pages.components.PageHeader import PageHeader
from src.pages.components.Tabs import Tabs
from src.utils.Settings import Settings
class DocumentationPage(BasePage):
    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="Documentation - Test Junkie",
                          directory="/documentation/")
        self.header = PageHeader()
        self.footer = PageFooter()
        self.floating_button = FloatingMenu()
        self.flash_msg = FlashMsg()
        self.cli_card = Tabs(container="//div[@id = 'cli']")
    def get_left_nav_links(self):
        """
        Gets all the links from the Left Navigation (as UiObjects)
        :return: LIST of UIObjects aka
                     [<src.pages.UiObject.UiObject instance at 0x02F4CCB0>,
                      <src.pages.UiObject.UiObject instance at 0x02F4CAF8>,
                      <src.pages.UiObject.UiObject instance at 0x02F4CC88>,
                      ...,
                      ...]
        """
        links = []
        for element in UiObject(By.XPATH, "//div[@id='leftCol']//a").get_elements():
            links.append(UiObject.from_web_element(element))
        return links
    def get_content_links_per_section(self, section_id=None):
        """
        Gets all the links on the page (as UiObjects) and maps them to their respective section
        :param section_id: STRING, section ID as appears in the DOM. Allows to get links for a specific section.
                                (Faster if you don't need links for all sections)
        :return: DICT, section to links mapping aka
                       {'cli': [<src.pages.UiObject.UiObject instance at 0x02F09BC0>,
                                <src.pages.UiObject.UiObject instance at 0x02F17940>,
                                <src.pages.UiObject.UiObject instance at 0x02F174B8>],
                        'section': [..., ..., ...],
                        'section': [..., ..., ...]}
        """
        def get_links():
            section_links = UiObject(By.XPATH, "//div[@id='content']/div[@id='{}']//a".format(section_id))
            _links = {section_id: []}
            if section_links.exists():
                for link in section_links.get_elements():
                    _links[section_id].append(UiObject.from_web_element(link))
            return _links
        if section_id:
            return get_links()
        links = {}
        section_xpath = "//div[@id='content']/div[contains(@class, 'section') and @id]"
        sections = UiObject(By.XPATH, section_xpath).get_elements()
        for element in sections:
            section_id = UiObject.from_web_element(element).get_attribute("id")
            links.update(get_links())
        return links