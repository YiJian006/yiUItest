from selenium import webdriver
from PIL import Image
from PIL import ImageEnhance
from aip import AipOcr # pip install baidu-aip
from time import sleep
class yzm:
    def __init__(self):
        self.APP_ID = '16838310'  # 替换为实际申请值
        self.API_KEY = '8GuIfzz8pSmg8x02GQNBWGyt'  # 替换为实际申请值
        self.SECRET_KEY = 'MoEeNimMbs9IB8bBB6SXrgjoogmpIzKI'

    def getyzm(self):
        coderange = (576,390,576+120,390+40) # 验证码坐标
        i = Image.open(r"C:\\Users\\yijian\Desktop\\selenium-master\\img\\aa.png") #打开截图
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
            return yz
        else:
            return "9999"

driver=webdriver.Chrome()


url = "http://eg77777.com/login"   #一般在登录首页
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)

driver.save_screenshot(r"C:\\Users\\yijian\\Desktop\\易建\\selenium-master\\img\\aa.png")  #截取当前网页，截得是全屏
driver.find_element_by_name("username").send_keys("ceshi")
driver.implicitly_wait(5)
driver.find_element_by_name("password").send_keys("qwer123")
f = yzm()
v = f.getyzm()
print(f)
driver.find_element_by_name("code").send_keys(v)
driver.find_element_by_css_selector("[type='submit']").click()
driver.implicitly_wait(5)
s = driver.find_element_by_xpath("//body//div[@class='v-snack__wrapper error']").text
print(s)
sleep(2)
print(driver.title)
driver.quit()
