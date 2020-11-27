# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
import time


class SeleniumMiddleware():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.path = 'C:\Program Files (x86)\Google\Chrome\Application\chromdriver.exe'
        self.browser = webdriver.Chrome()
        self.browser.set_window_size(1400, 700)
        self.browser.set_page_load_timeout(self.timeout)
        self.wait = WebDriverWait(self.browser, self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self, request, spider):
        """
        用PhantomJS抓取页面
        :param request: Request对象
        :param spider: Spider对象
        :return: HtmlResponse
        """
        self.logger.debug('PhantomJS is Starting')
        page = request.meta.get('page', 1)
        print('正在获取第', page, '页')
        try:
            self.browser.get(request.url)

            # 滚动条下拉到底
            self.browser.execute_script("document.documentElement.scrollTop=10000")
            # 等待网页加载完毕
            time.sleep(5)


            if page > 1:
                input = self.wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="pnum"]')))  # 获取输入页面数框
                submit = self.wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="pagebar"]/input[2]')))  # 获取确定按钮
                input.clear()
                input.send_keys(page)
                time.sleep(1)

                submit.click()
                # next = self.wait.until(
                #     EC.element_to_be_clickable((By.XPATH, '//*[@id="pager"]/span[10]')))  # 获取确定按钮
                # next.click()

                # 滚动条下拉到底，第二种写法
                # self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                time.sleep(5)

            # self.wait.until(
            #     EC.text_to_be_present_in_element((By.XPATH, './/span[@class="p-num"]/a[@class="curr"]'), str(page)))

            # 等待加载完所有的商品list 然后进一步解析
            # self.wait.until(EC.element_to_be_clickable((By.XPATH, './/span[@class="p-skip"]/a')))

            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)


    @classmethod
    def from_crawler(cls, crawler):
        return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
                   )
