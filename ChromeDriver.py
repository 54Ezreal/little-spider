import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chromium.webdriver import ChromiumDriver

import time

import ChromeConfig


class ChromeDriver:
    client: ChromiumDriver = None

    def __init__(self):
        if self.client is not None:
            self.client.quit()

        self.init_chrome_options()

    def init_chrome_options(self):
        chrome_options = webdriver.ChromeOptions()

        if ChromeConfig.debugger_address is None:
            # 取消Chrome正受到自动测试软件的控制的提示
            chrome_options.add_experimental_option("excludeSwitches",
                                                   ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension',
                                                   False)

        for item in ChromeConfig.chrome_arguments:
            chrome_options.add_argument(item)

        if ChromeConfig.debugger_address is not None:
            chrome_options.add_experimental_option(
                "debuggerAddress", ChromeConfig.chrome_debugger_address)

        self.client = webdriver.Chrome(ChromeDriverManager().install(),
                                       options=chrome_options)

        if ChromeConfig.windows_size is not None:
            self.client.set_window_size(size['w'], size['h'])
        else:
            size = random.choice(ChromeConfig.windows_sizes)
            self.client.set_window_size(size['w'], size['h'])

        with open('stealth.min.js') as f:
            js = f.read()

        self.client.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument",
                                    {"source": js})

    def test(self):
        """测试爬虫伪装程度
        """
        self.client.get('https://bot.sannysoft.com/')
        time.sleep(10)
        self.client.save_screenshot('sannysoft.png')

        source = self.client.page_source
        with open('sannysoft.html', 'w') as f:
            f.write(source)

        self.client.get(
            'https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html'
        )
        time.sleep(5)
        self.client.save_screenshot('intoli.png')

        source = self.client.page_source
        with open('intoli.html', 'w') as f:
            f.write(source)

    def check_dom_exist(self, dom, dom_type='xpath', wait_time=60) -> bool:
        """
        确认dom是否存在
        """
        try:
            if dom_type == 'xpath':
                WebDriverWait(self.client, wait_time).until(
                    EC.presence_of_element_located((By.XPATH, dom)))
            elif dom_type == 'css':
                WebDriverWait(self.client, wait_time).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, dom)))
            elif dom_type == 'id':
                WebDriverWait(self.client, wait_time).until(
                    EC.presence_of_element_located((By.ID, dom)))
            return True
        except:
            return False

    def exec_script(self, dom, script, wait_time=60, dom_type='xpath'):
        """
        执行页面脚本
        """
        if dom_type == 'xpath':
            element = WebDriverWait(self.client, wait_time).until(
                EC.presence_of_element_located((By.XPATH, dom)))
            return self.client.execute_script(script, element)
        if dom_type == 'css':
            element = WebDriverWait(self.client, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, dom)))
            return self.client.execute_script(script, element)
        return None

    def find_element(self, dom, dom_type='xpath', wait_time=60):
        element = None
        if dom_type == 'xpath':
            element = WebDriverWait(self.client, wait_time).until(
                EC.presence_of_element_located((By.XPATH, dom)))
        if dom_type == 'css':
            element = WebDriverWait(self.client, wait_time).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, dom)))
        return element

    def click_by_offset(self, x, y, left_click=True):
        """
        鼠标点击指定坐标
        """
        if left_click:
            ActionChains(self.client).move_by_offset(x, y).click().perform()
        else:
            ActionChains(self.client).move_by_offset(
                x, y).context_click().perform()

    def dom_xpath_clean_key(self, xpath, wait_time=30):
        """
        按键操作
        :param xpath:
        :param wait_time:
        """
        WebDriverWait(self.client, wait_time).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        self.client.find_element_by_xpath(xpath).clear()

    def dom_xpath_send_key(self, xpath, keys, wait_time=30):
        """
        按键操作
        :param xpath:
        :param keys:
        :param wait_time:
        """
        WebDriverWait(self.client, wait_time).until(
            EC.presence_of_element_located((By.XPATH, xpath)))
        self.client.find_element_by_xpath(xpath).send_keys(keys)

    def action_scroll(self,
                      scroll_times=30,
                      scroll_step=500,
                      full_scroll=False,
                      sleep_time=0.1):
        """
        屏幕滚动操作
        :param scroll_times: 滚动次数
        :param scroll_step: 滚动长度
        :param full_scroll: 是否滚动到底部
        :param sleep_time:
        """
        for i in range(0, int(scroll_times)):
            self.client.execute_script('window.scrollBy(0,' +
                                       str(scroll_step) + ')')
            time.sleep(sleep_time)
        if full_scroll:
            self.client.execute_script('window.scrollBy(0,100000)')
