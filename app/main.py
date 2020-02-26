# http://depremonlemleri.com/

# uavt kodu nedir
# evim depreme dayanıklı mı

import random
import time

from utils import logger
from utils import webdriver



GOOGLE_SEARCH_KEYWORDS = [
    'evim depreme dayanıklı mı',
    'uavt kodu nedir'
]


GOOGLE_SEARCH_MAIN_DOMAIN = 'http://depremonlemleri.com/'


def main():
    main_logger = logger.Logger('main', __name__).logger
    user_agent = random.choice(USER_AGENTS)
    selenium_driver = SeleniumWebDriver(user_agent, main_logger)
    selenium_driver.create_webdriver()
    selenium_driver.open_url(GOOGLE_BASE)
    time.sleep(5)
    search_bar_elem = selenium_driver.find_element('find_element_by_name', 'q')
    selenium_driver.click_element(search_bar_elem)
    search_phrase = random.choice(GOOGLE_SEARCH_KEYWORDS)
    selenium_driver.send_keys(search_bar_elem, search_phrase)
    search_button = selenium_driver.find_element('find_element_by_name', 'btnK')
    selenium_driver.click_element(search_button)

    time.sleep(5000)


main()
