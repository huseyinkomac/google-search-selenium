import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class SeleniumWebDriver:
    def __init__(self, user_agent, logger):
        self.user_agent = user_agent
        self.logger = logger

    def create_webdriver(self, headless=True):
        if headless:
            os.environ['MOZ_HEADLESS'] = '1'
        try:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", self.user_agent)
            profile.set_preference("dom.webnotifications.enabled", False)

            profile.update_preferences()
            
            self.driver = webdriver.Firefox(firefox_profile=profile)
            self.driver.set_window_size(1280, 1024)
            self.driver.delete_all_cookies()
        except Exception as e:
            self.logger.error(f"Couldn't create webdriver with error {str(e)}")

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, elem):
        elem.click()
        # find_method.click(elem)
        # self.driver.find_ele

    def find_element(self, method, identifier):
        find_method = getattr(self.driver, method)
        elem = find_method(identifier)
        return elem

    def send_key(self, elem, key):
        elem.send_keys(key)

    def send_keys(self, elem, keys):
        for key in keys:
            elem.send_keys(key)
            time.sleep(random.uniform(0.2, 0.7))

    def close_webdriver(self):
        self.driver.close()
        self.driver.quit()
