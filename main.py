# http://depremonlemleri.com/

# uavt kodu nedir
# evim depreme dayanıklı mı

import os

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


GOOGLE_SEARCH_KEYWORDS = [
    'evim depreme dayanıklı mı',
    'uavt kodu nedir'
]

GOOGLE_SEARCH_MAIN_DOMAIN = 'http://depremonlemleri.com/'


class SeleniumWebDriver:
    def __init__(self, user_agent):
        self.user_agent = user_agent

    def create_webdriver(self):
        try:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", self.user_agent)
            profile.set_preference("dom.webnotifications.enabled", False)

            profile.update_preferences()
            os.environ['MOZ_HEADLESS'] = '1'
            self.driver = webdriver.Firefox(firefox_profile=profile)
            self.driver.set_window_size(1280, 1024)
            self.driver.delete_all_cookies()
        except Exception as e:
            self.logger.error(f"Couldn't create webdriver with error {str(e)}")

    def open_url(self, url):
        self.driver.get(url)

    def close_webdriver(self):
        self.driver.close()
        self.driver.quit()


def main():



main()
