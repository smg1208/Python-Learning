from src.pages.BasePage import BasePage
from src.pages.components.FlashMsg import FlashMsg
from src.pages.components.FloatingMenu import FloatingMenu
from src.pages.components.PageFooter import PageFooter
from src.pages.components.PageHeader import PageHeader
from src.pages.components.Tabs import Tabs
from src.utils.Settings import Settings
class GetStartedPage(BasePage):
    def __init__(self):
        BasePage.__init__(self,
                          domain=Settings.DOMAIN,
                          title="Get Started - Test Junkie",
                          directory="/get-started/")
        self.header = PageHeader()
        self.footer = PageFooter()
        self.floating_button = FloatingMenu()
        self.flash_msg = FlashMsg()
        self.installation_card = Tabs(container="//div[@id = 'installation']")
        self.usage_card = Tabs(container="//div[@id = 'basic_usage']")
        self.test_execution_card = Tabs(container="//div[@id = 'test_execution']")