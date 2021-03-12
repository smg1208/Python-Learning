from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# chrome_options = webdriver.ChromeOptions()
# chrome_options.set_capability("browserVersion", "83")
# chrome_options.set_capability("browserName", "chrome")
# chrome_options.set_capability("platformName", "WIN10")
driver = webdriver.Remote(
    command_executor='http://192.168.1.6:20784/wd/hub',
    # command_executor='http://192.168.1.6:20784',
    # options=chrome_options
    desired_capabilities=DesiredCapabilities.CHROME
)
driver.get("http://www.google.com")
driver.quit()  