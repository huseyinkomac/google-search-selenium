# http://depremonlemleri.com/

# uavt kodu nedir
# evim depreme dayanıklı mı

import random
import time

from utils import logger
from utils import webdriver
from utils import constants


class GoogleSearchBot:
    def __init__(self):
        self.logger = logger.Logger('main', __name__).logger
        self.user_agent = random.choice(constants.USER_AGENTS)
        self.driver = webdriver.SeleniumWebDriver(self.user_agent, self.logger)
        self.current_page_num = 1
        self.search_finished = False
        self.found_elem = None

    def get_url_dict_from_search_result(self, search_result):
        clickable_elem = self.driver.find_element_in_element(search_result, 'find_element_by_tag_name', 'a')
        url_dict = {}
        url_dict['url'] = str(clickable_elem.get_attribute('href'))
        url_dict['elem'] = clickable_elem
        return url_dict

    def get_all_url_dicts_from_curr_page(self):
        parent_divs = self.driver.find_element('find_elements_by_class_name', 'srg')
        search_results_div_parts = [self.driver.find_element_in_element(parent_div, 'find_elements_by_class_name', 'g') for parent_div in parent_divs]
        search_results = [item for div_part in search_results_div_parts for item in div_part]
        url_dicts = [self.get_url_dict_from_search_result(search_result) for search_result in search_results]
        self.logger.info(f"Search results {str(url_dicts)}")
        return url_dicts

    def enter_found(self):
        self.found_elem['elem'].click()
        self.logger.info(f"Entered found page succesfully {str(self.found_elem['url'])}")

    def get_all_hrefs(self):
        all_tag_as = self.driver.find_element('find_elements_by_tag', 'a')
        

    def go_around_in_found(self):
        endpoint_count = random.randint(3, 5)
        for _ in range(endpoint_count):
            clickable_href = random.choice(self.get_all_hrefs())
            clickable_href.click()
            time.sleep(random.uniform(3.0, 6.0))

    def search_page(self):
        '''
        Searches google result page
        finishes searching if found
        '''
        self.logger.info(f"Searching page num {self.current_page_num}")
        url_dicts = self.get_all_url_dicts_from_curr_page()
        for url_dict in url_dicts:
            if constants.GOOGLE_SEARCH_MAIN_DOMAIN in url_dict['url']:
                self.found_elem = url_dict
                self.search_finished = True

        self.logger.info(
            "Couldn't find given url with search keyword "
            f"{self.main_search_phrase} in page num {self.current_page_num}"
        )

    def go_to_next_page(self):
        self.logger.info(
            f"Done searching for page num {str(self.current_page_num)} "
            "Going into next page."
        )
        self.current_page_num += 1
        next_page_elem = self.driver.find_element(
            'find_element_by_xpath',
            f'//a[@aria-label="Page {str(self.current_page_num)}"]'
        )
        self.driver.click_element(next_page_elem)

    def search_keyword(self):
        search_bar_elem = self.driver.find_element('find_element_by_name', 'q')
        self.driver.click_element(search_bar_elem)
        self.driver.send_keys(search_bar_elem, self.main_search_phrase)
        search_button = self.driver.find_element('find_element_by_name', 'btnK')
        self.driver.click_element(search_button)

    def start(self):
        self.driver.create_webdriver(headless=False)
        self.driver.open_url(constants.GOOGLE_BASE)
        time.sleep(5)
        self.main_search_phrase = random.choice(constants.GOOGLE_SEARCH_KEYWORDS)
        self.search_keyword()
        self.search_page()

        while not self.search_finished:
            self.go_to_next_page()
            self.search_page()

        if self.found_elem:
            self.logger.info(f"Page found {str(self.found_elem['url'])}")
            self.enter_found()
            self.go_around_in_found()
            self.logger.info(f"Task sucessfully finished with keyword {self.main_search_phrase}")

        else:
            self.logger.error(f"Couldn't find page in any result with keyword {self.main_search_phrase}")


if __name__ == '__main__':
    search_bot = GoogleSearchBot()
    search_bot.start()

'''
go around in found
a rel->home click

'''
