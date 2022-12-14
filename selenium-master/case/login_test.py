from time import time
from bussinses.funnicgong import Login_tes
import ddt,unittest,os
from util import  log
from selenium import webdriver
from util.gettestdata import huoqu_test
from selenium.webdriver.chrome.options import Options
from time import sleep

path=os.getcwd()
case_path=path+'\\data\\case.xlsx'
casedata=huoqu_test(case_path,0)
print(casedata)

@ddt.ddt
class Testlogin(unittest.TestCase):
    def setUp(self):
        option = Options()
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('--disable-blink-features=AutomationControlled')
        self.logs=log.log_message()
        self.derve=webdriver.Chrome(options=option)
        sleep(3)
        self.derve.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """Object.defineProperty(navigator, 'webdriver', {get: () => undefined})""",
    })
        self.login_fun=Login_tes(self.derve)
 
    @ddt.data(*casedata)
    def test_login1(self,casedata):
        self.name=casedata['username']
        self.pwd=casedata['pwd']
        self.suc=casedata['suc']
        self.assert_value = casedata['assert']
        self.derve.get_screenshot_as_file(path+'\\resultpang\\%s.png'%casedata)
        self.logs.info_log('input data:name:%s,pwd:%s,suc:%s,assert:%s' % (self.name, self.pwd, self.suc, self.assert_value))
        self.re_data = self.login_fun.login(self.suc,self.name, self.pwd)
        # if self.re_data[0] == None:
        #     self.assertEqual(self.re_data[1], "验证码错误")
        self.assertEqual(self.re_data, self.assert_value)
    def tearDown(self):
        self.derve.quit()
