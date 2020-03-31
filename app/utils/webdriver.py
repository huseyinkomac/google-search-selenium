import os
import time
import random
import socket

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException


class SeleniumWebDriver:
    def __init__(self, user_agent, logger, proxies=None):
        self.user_agent = user_agent
        self.logger = logger
        self.proxies = proxies

    def create_webdriver(self, headless=True):
        if headless:
            os.environ['MOZ_HEADLESS'] = '1'
        try:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("general.useragent.override", self.user_agent)
            profile.set_preference("dom.webnotifications.enabled", False)

            if self.proxies:
                ip = self.proxies['ip']
                port = int(self.proxies['port'])
                profile.set_preference("network.proxy.type", 1)
                profile.set_preference("network.proxy.http", ip)
                profile.set_preference("network.proxy.http_port", port)
                profile.set_preference("network.proxy.ssl", ip)
                profile.set_preference("network.proxy.ssl_port", port)

            profile.update_preferences()

            self.driver = webdriver.Firefox(firefox_profile=profile)
            socket.setdefaulttimeout(60)
            self.driver.set_window_size(1280, 1024)
            self.driver.delete_all_cookies()
        except Exception as e:
            self.logger.error(f"Couldn't create webdriver with error {str(e)}")

    def open_url(self, url):
        self.driver.get(url)

    def click_element(self, elem):
        elem.click()

    def find_element(self, method, identifier):
        find_method = getattr(self.driver, method)
        try:
            elem = find_method(identifier)
        except NoSuchElementException:
            return None
        return elem

    def find_element_in_element(self, source_elem, method, identifier):
        find_method = getattr(source_elem, method)
        try:
            elem = find_method(identifier)
        except NoSuchElementException:
            return None
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
