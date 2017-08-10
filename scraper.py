from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time, datetime

class Scraper:
    def __init__(self, driver_path = "C:\Python34\chromedriver_win32\chromedriver.exe", url_path=""):
        self.driver_path = driver_path
        self.url_path = url_path
        self.browser = webdriver.Chrome(self.driver_path)
        self.status = [-1, ('unintialized target', -1, 'no target element')]
        self.initialize_time = (datetime.datetime.now(), time.tzname)

    def __repr__(self):
        return("Scraper Bot with '%s' \nwebdriver/n driver path =  '%s' \ncurrent target url: '%s' \nurl_status:'%s's" % ('Chrome',self.driver_path,self.url_path,self.status))

    def set_url(self,url_target):
        self.url_path = str(url_target)
        return(True)

    def get_url(self):
        return self.url_path

    def set_status(self, status_update):
        self.status[0] = status_update[0]
        self.status[1] = status_update[1]
        return(True)

    def get_status(self):
        return(self.status)

    def get_time_stamp(self):
        return(self.initialize_time)

    def scrape_target(self, input_url, wait_time, target_element, err_code='error-code'):
        self.set_url(input_url)
        self.browser.get(self.get_url())
        if (self.browser.find_elements_by_class_name(err_code)):
            self.set_status([0,('error', 404, err_code)])
            return
        try:
            element = WebDriverWait(self.browser,wait_time).until(EC.presence_of_element_located((By.CLASS_NAME,str(target_element))))
        except TimeoutException:
            self.set_status([0,('timeout-error', wait_time, target_element)])
        else:
            self.set_status([1,('success', self.get_url(), target_element)])

    def get_page_source(self):
        return(self.browser.page_source)

    def return_page_source(self, return_info):
        return_info.append(self.get_status())
        return_info.append(self.get_page_source())
        return(return_info)

    def browser_tear_down(self):
        self.browser.quit()
#
s = Scraper()
info=[]
s.scrape_target('http://steamcommunity.com/market/listings/730/Krakow%202017%20Legends%20Autograph%20Capsule',5,'market_commodity_orders_block')
s.return_page_source(info)
#'market_listing_row_link','market_commodity_orders_block'
# #class Scraper_Bot(Scraper):
