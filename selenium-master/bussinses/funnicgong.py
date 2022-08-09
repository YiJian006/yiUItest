from tkinter import Button
import yaml,os
path = os.getcwd()
# from selenium import webdriver
from util import log
import time
from selenium.webdriver.common.keys import Keys
from PIL import Image
from PIL import ImageEnhance
from aip import AipOcr # pip install baidu-aip
from time import sleep
from selenium.webdriver import ChromeOptions,ActionChains




# 登录模块封装
class Login_tes:
    print("eee")
    def __init__(self,driver):
        self.driber = driver
        self.logs = log.log_message()
        self.file = open(path+"\\data\\page_data.yaml", "r",encoding= "utf-8")
        self.data = yaml.load(self.file)
        self.file.close()
        self.lo_url = self.data["login"].get('url')
        self.denglu1 = self.data["login"].get('denglu1')
        self.denglu2 = self.data["login"].get('denglu2')
        self.username = self.data["login"].get('username')
        self.password = self.data["login"].get('password')
        self.button = self.data["login"].get("button")
        self.lo_err = self.data["login"].get('login_err')
        self.driber.get(self.lo_url)
        self.driber.maximize_window()
        

    def login(self,suc,username,password):
        try:
            self.driber.implicitly_wait(10)
            self.driber.find_element_by_xpath(self.denglu1).click()
            self.driber.find_element_by_xpath(self.denglu2).click()
            self.driber.find_element_by_xpath(self.username).send_keys(username)
            self.driber.find_element_by_xpath(self.password).send_keys(password)
            self.driber.find_element_by_xpath(self.button).click()

            # 通过css定位滑动坐标
            slider = self.driber.find_element_by_id("nc_1_n1z")
            sleep(1)
            action = ActionChains(self.driber)
            # 长按鼠标
            action.click_and_hold(slider)
            # 偏移量（F12中查看）
            action.move_by_offset(260, 0)
            # 释放鼠标
            action.release()
            # 执行以上操作
            action.perform()
            self.driber.implicitly_wait(10)
            sleep(1)
            self.driber.save_screenshot(r"C:\\Users\\yijian\Desktop\\selenium-master\\img\\aa.png")
            self.driber.implicitly_wait(10)
            if suc == "1":
                # self.login_su = self.driber.title
                self.login_su = self.driber.current_url
                return self.login_su
            if suc == "2":
                self.driber.implicitly_wait(5)
                # 定位自动消失元素sources-点击暂停即可定位
                self.login_err = self.driber.find_element_by_xpath(self.lo_err).text
                return self.login_err
        except Exception as e:
            self.logs.error_log('用例执行失败，原因：%s'%e)
        finally:
            self.driber.quit()