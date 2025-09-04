import os
import time
from string import Template
from typing import List


import yaml
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy as By
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from appium.webdriver.webelement import WebElement
from AutoDroid.common.handle_black import handle_black
from AutoDroid.common.log import Logger

logger = Logger().get_logger()


class BasePage:

    def __init__(self, driver: WebDriver = None):

        if not driver:  # 如果没有传递driver
            desire = {
                "platformName": "Android",
                "deviceName": "emulator-5554",
                "appPackage": "com.xueqiu.android",
                "appActivity": "view.WelcomeActivityAlias"
            }
            self.driver = webdriver.Remote('http://192.168.124.39:4723/wd/hub', desire)
            self.driver.implicitly_wait(10)

        else:
            self.driver = driver

    # 元素定位交互方法封装
    # 查找单个元素
    @handle_black
    def find(self, by, locator) -> WebElement:
        by = by.lower()
        if by == "resource-id":  # resource-id
            by_locator = (By.ID, locator)
        elif by == "content-desc":
            by_locator = (By.ACCESSIBILITY_ID, locator)
        elif by == "class":
            by_locator = (By.CLASS_NAME, locator)
        elif by == "xpath":
            by_locator = (By.XPATH, locator)
        else:
            raise AttributeError(f"元素定位方式未找到，你传入的是{by}")
        # ele = self.driver.find_elements(*by_locator)
        ele = WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(by_locator), message="元素定位异常")
        return ele

    # 查找多个元素
    @handle_black
    def finds(self, by, locator) -> List[WebElement]:
        by = by.lower()
        if by == "resource-id":  # resource-id
            by_locator = (By.ID, locator)
        elif by == "content-desc":
            by_locator = (By.ACCESSIBILITY_ID, locator)
        elif by == "class":
            by_locator = (By.CLASS_NAME, locator)
        elif by == "xpath":
            by_locator = (By.XPATH, locator)
        else:
            raise AttributeError(f"元素定位方式未找到，你传入的是{by}")
        # ele = self.driver.find_element(*by_locator)
        ele_s = WebDriverWait(self.driver, 10).until(ec.visibility_of_all_elements_located(by_locator),
                                                     message="元素定位异常")
        return ele_s

    # 查找单个元素，进行点击
    @handle_black
    def find_and_click(self, by, locator):
        self.find(by, locator).click()

    # 查找多个元素，对其中一个进行点击
    @handle_black
    def finds_and_click(self, by, locator, index):
        self.finds(by, locator)[index].click()

    # 查找单个元素，输入文本
    @handle_black
    def find_and_send(self, by, locator, text):
        self.find(by, locator).send_keys(text)

    # 查找多个元素，对其中一个进行输入
    @handle_black
    def finds_and_send(self, by, locator, index, text):
        self.finds(by, locator)[index].send_keys(text)

    # 查找单个元素，清空文本内容
    @handle_black
    def find_and_clear(self, by, locator):
        self.find(by, locator).clear()

    # 查找多个元素，清空其中一个
    @handle_black
    def finds_and_clear(self, by, locator, index):
        self.finds(by, locator)[index].clear()

    # 上下左右滑动
    def swipe_lrdu(self, direction, scale, t=300):  # 0.8
        size = self.driver.get_window_size()
        width = size["width"]  # 810
        height = size["height"]  # 1000

        x, y = width * 0.5, height * 0.5

        if direction == "up":  # 1300*0.8
            x1 = x
            x2 = x
            y1 = y + height * scale * 0.5
            y2 = y - height * scale * 0.5

        elif direction == "down":
            x1 = x
            x2 = x
            y1 = y - height * scale * 0.5
            y2 = y + height * scale * 0.5

        elif direction == "left":
            y1 = y
            y2 = y
            x1 = x + width * scale * 0.5
            x2 = x - width * scale * 0.5

        elif direction == "right":
            y1 = y
            y2 = y
            x2 = x + width * scale * 0.5
            x1 = x - width * scale * 0.5
        else:
            raise AttributeError(f"滑动方向错误，你滑动的方向是{direction}")

        self.driver.swipe(x1, y1, x2, y2, t)



    @staticmethod
    def get_yaml_path(yaml_file_name):
        path = os.path.abspath(__file__)  # 获取base_page.py的绝对路径， 会随着项目位置的不同，自动变化
        py_page_path = os.path.dirname(path)  # 获取base_page.py所在的文件夹 py_page
        project_path = os.path.dirname(py_page_path)  # py_page所在的文件夹
        yam_path = project_path + fr"\py_yaml\{yaml_file_name}"
        # yam_path = os.path.join(project_path, "py_yaml", yaml_file_name)
        return yam_path


if __name__ == '__main__':
    pass
    # basepage = BasePage()
    # p = BasePage.get_yaml_path("main_page.yaml")
    # basepage.run_steps(p, "agree",tel="13012312300.")
    # time.sleep(10)
    #
    # basepage.find_and_click(By.XPATH, "//*[@text='同意']")
    # time.sleep(10)
    #
    # basepage.driver.quit()

    # basepage.swipe_lrdu("up",0.8)
    # time.sleep(3)
    # basepage.swipe_lrdu("down",0.6)
    # time.sleep(1)
    #
    # basepage.swipe_lrdu("left",0.8)
    # time.sleep(1)
    #
    # # basepage.swipe_lrdu("aaaa",0.8)
    # time.sleep(3)
