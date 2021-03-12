from selenium.webdriver.common.by import By


class AboutUsPageLocators(object):
    MAIN_CONTENT = (By.CLASS_NAME, 'elementor-section-wrap')
    PASSSTER_FORM = (By.CLASS_NAME, 'passster-form')
    PASSSTER_PASSWORD_INPUT = (By.CLASS_NAME, 'passster-password')
    PASSSTER_SUBMIT = (By.CLASS_NAME, 'passster-submit')
    PASSSTER_ERROR = (By.CLASS_NAME, 'passster-error')
