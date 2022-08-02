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

# 验证码
class yzm:
    def __init__(self):
        self.APP_ID = '16838310'  # 替换为实际申请值
        self.API_KEY = '8GuIfzz8pSmg8x02GQNBWGyt'  # 替换为实际申请值
        self.SECRET_KEY = 'MoEeNimMbs9IB8bBB6SXrgjoogmpIzKI'

    def getyzm(self):
        coderange = (576,390,576+120,390+40) # 验证码坐标
        i = Image.open(r"C:\\Users\\yijian\Desktop\\selenium-master\\img\\aa.png") # 打开截图
        frame4 = i.crop(coderange)  #使用Image的crop函数，从截图中再次截取我们需要的区域
        frame4.save(r"C:\\Users\\yijian\Desktop\\selenium-master\\img\\aa.png")    #保存截图
        i2 = Image.open(r"C:\\Users\\yijian\Desktop\\selenium-master\\img\\aa.png")  #打开截图
        imgry = i2.convert('L')   #图像加强，二值化，PIL中有九种不同模式。分别为1，L，P，RGB，RGBA，CMYK，YCbCr，I，F。L为灰度图像
        sharpness = ImageEnhance.Contrast(imgry) #对比度增强
        i3 = sharpness.enhance(3.0)  #3.0为图像的饱和度
        i3.save(r"C:\\Users\\yijian\Desktop\\selenium-master\\img\\image_code.png")
        img = open(r"C:\\Users\\yijian\\Desktop\\selenium-master\\img\\image_code.png","rb").read()
        result = AipOcr(self.APP_ID, self.API_KEY, self.SECRET_KEY).webImage(img)
        print(result)
        yz = int(result['words_result'][0]['words'])
        if isinstance(yz,int):
            if yz < 1000:
                return None
            return yz
        else:
            return None

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
        self.denglu = self.data["login"].get('denglu')
        self.username = self.data["login"].get('name')
        self.password = self.data["login"].get('password')
        self.code = self.data["login"].get("code")
        self.lo_err = self.data["login"].get('login_err')
        self.driber.get(self.lo_url)
        self.driber.maximize_window()
        self.yz = yzm()

    def login(self,suc,name,password):
        try:
            self.driber.implicitly_wait(10)
            self.driber.find_element_by_name(self.username).send_keys(name)
            self.driber.find_element_by_name(self.password).send_keys(password)
            self.driber.implicitly_wait(10)
            sleep(1)
            self.driber.save_screenshot(r"C:\\Users\\yijian\Desktop\\selenium-master\\img\\aa.png")
            self.driber.implicitly_wait(10)
            self.yzm = self.yz.getyzm()
            if self.yzm == None:
                self.driber.find_element_by_name(self.code).send_keys(9999)
                self.driber.find_element_by_css_selector(self.denglu).click()
                self.driber.implicitly_wait(10)
                self.login_err = self.driber.find_element_by_xpath(self.lo_err).text 
                L = [None,self.login_err]
                return L
            self.driber.implicitly_wait(10)
            self.driber.find_element_by_name(self.code).send_keys(self.yzm)
            self.driber.implicitly_wait(10)
            self.driber.find_element_by_css_selector(self.denglu).click()
            if suc == "1":
                self.login_su = self.driber.title
                # self.login_su = self.driber.find_element_by_class_name(self.lo_err).text
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