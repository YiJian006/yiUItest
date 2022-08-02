# from selenium import webdriver

# d = webdriver.Chrome()
# d.get("https://www.baidu.com")
# d.find_element_by_css_selector("#s-top-left > a:nth-child(4)").click()

# def fn(s):
#     l = s.split(" ")
#     return len(l[-1])

# print(fn(" QEFF"))
# while True:
#     try:
#         i = int(input())
#         l = []
#         for j in range(i):
#             l.append(int(input()))
#         s = set(l)
#         l2 = [x for x in s]
#         l2.sort()
#         for j in l2:
#             print(j)
#     except:
#         break

# while True:
#     try:
#         s = input()
#         l = list(s)
#         L = []
#         for j in range(0,len(s),8):
#             L.append("".join(l[j:j+8]))
#         print(L)
#         if len(L[-1]) == 8:
#             pass
#         elif len(L[-1]) < 8:
#             for i in range(8-len(L[-1])):
#                 L[-1] += "0"
#         for n in L:
#             print(n,end="\n")
#     except:
#         break
# s = "qwedfvbhu1edvghbnk"
# l = list(s)


# L = []
# for j in range(0,len(s),8):
#     L.append("".join(l[j:j+8]))
# print(L)

# s = input()
# l = s.split(" ")
# L = []
# for i in l:
#     L.append(i[::-1])

# print(" ".join(L))

# s = input()
# se = set(list(s)[::-1])
# l = [x for x in se]
# print(int("".join(l)))

# dic = {1:2,3:6,7:8,5:3}
# print(sorted(dic))
# for k in sorted(dic):
#     print(k,dic.get(k))
# a=input()
# s = input()
# l = s.split(";")
# print(l)
# print(int("22"))
# if int("22"):
#     print(5)
# s = input()
# l = s.split(";")
# L = [0,0]
# for i in l:
#     if i == "":
#         pass
#     else:
#         if len(i) > 3:
#             pass
#         elif i[0] == "A" and i[1:].isdigit():
#             L[0] = L[0] - int(i[1:])
#         elif i[0] == "D" and i[1:].isdigit():
#             L[0] = L[0] + int(i[1:])
#         elif i[0] == "W" and i[1:].isdigit():
#             L[1] = L[1] + int(i[1:])
#         elif i[0] == "S" and i[1:].isdigit():
#             L[1] = L[1] - int(i[1:])
#         else:
#             pass
# print(L[0],L[1])

# s = R'''D:\zwtymj\xccb\ljj\cqzlyaszjvlsjmkwoqijggmybr 645
# E:\je\rzuwnjvnuz 633
# C:\km\tgjwpb\gy\atl 637
# F:\weioj\hadd\connsh\rwyfvzsopsuiqjnr 647
# E:\ns\mfwj\wqkoki\eez 648
# D:\cfmwafhhgeyawnool 649
# E:\czt\opwip\osnll\c 637
# G:\nt\f 633
# F:\fop\ywzqaop 631
# F:\yay\jc\ywzqaop 631'''
# l = s.split("\n")
# d = {}


# for i in l:
#     l1 = i.split(" ")
#     # print(l1)
#     print((l1[0].split("\\"))[-1])

# for i in l:
#     if len(d) > 18:
#         break
#     else:
#         l1 = i.split(" ")
        
#         if len((l1[0].split("\\"))[-1]) > 16:
#             x = (l1[0].split("\\"))[-1][-16::]
#             # print(x)
#             d[x+" "+l1[-1]]=d.get(x+" "+l1[-1],0) +1
#         else:
#             y = (l1[0]).split("\\")
#             # print(y)
#             d[y[-1]+" "+l1[-1]]=d.get(y[-1]+" "+l1[-1],0) +1
# for k,v in d.items():
#     print(str(k)+" "+str(v))

# s = "473 bb daccb caddd bddc c baa adb ad abbcb cdaa abab a abcc ddcbd cadcc cdacd aaa a b acccd bbb dacc cc acbdd bcbb ba bacaa adda acd aaad d ab acac bc dabab abcd aacba aba daa bb ad cddab a bbaa aacad cdac acbcc cada bacd adcad cdadc bcbcc aa b acd cbaac ddcd ccb dac a dac adbcb bcda dda a ab ca dd d abd a dbb ccabd bdddd abd adc aaa baccb ccdcd a da c cadc dcdbd d aa bb a cac c ad adb ca cdcc cadd dddca d cba cb caab caa dd cd bca abc cdaa cdb bad dad bda d ddbc dab baaa adaac b a dbccd bd b bdad cdacd baa ac ddcad d bb acc aa cd cbdbb bbbcb a cc aacc c aadc dbcd a bca dd abbb ccdcd ccd ab d a a dadcd dbd bcaa c cda b ddab caaaa cdcdb b acbc ccaa dabca dcd b ba dbcc da bdbcc ab abaca bb cddc caca da dadba accdd bdac dbcd bcbbd ab bd ccb ddaa aa b b d bddd cabac aaba ab ccdb db abbd ada bdadb c abba dd cdb bca cccda badba abaa ac aabad db ccbad bddd ada dba acba b bc dd bbbbd cc cbdd cd abcaa bb ddaca acadb bbbb bddcc bdada aaa bcbda c aaa aadd cdddc adb cdbab c cbca bb aacab acdb bbdab b acbda cbdcd bda bacdc db d adcbd bccc c aaa cdd bdcd bac a aaab ddbb cd ccdbb addcc cdc c ca baadc addba dbdbd dba bbdda bcb c cdad aacac dcada cb aaad a cccab caca aad bbb dd b babbb cba bdaca db bacd bc bcbda cdda bcccd bdcda bdbcd adb cbcb a c bacba abbb adab adab b b d bca badbc baa cdb b abc aabb b d c cdab cacda d cdcda adcdc bcc bbccd b adb caba cbaaa aadb dcc add bcac bacbd bb a b c cabaa c caad c aa bcc ccab ddc dadca cdcba aaba dabbd dcb a bddb bb a c c cbc ccd dd a cabbb b caadb cb dca cbb ddaa bcadc dab a bbda cd bc ccad bbd ab c acddd cdd dbbbb daaab abbb cabc add ca caa bbbb dcab daaaa baca dcd ccacb ba bddaa acac dbcc bcc cbbcc b abba daa dbab bcca ba aa d dcdc d dcaa cbcda bd b ccbcb baa dcacd d c cbda baba d abb c cbdc da dbbb cd aabc dadc b a ddb c ddd ccdc ccd cba dbaac dcccd ddbac dbbdd bad bcdd cb dac dccd d a acdd d c cb b bcbb c a aca bcba d d bbdbc d c dabad ccca dc adb ddb dcdd dba ad ddaba c ac ddac bbbd cd a dacbb 1"
# l = s.split(" ")
# l1 = l[1:int(l[0])+1]
# L = []
# x = sorted(list(l[-2]))
# y = int(l[-1])
# # print(x)
# for i in l1:
#     if sorted(list(i)) == x and i != l[-2]:
#         L.append(i)
# a=""
# if l1[y] in L:
#     a = l1[y]

# print(len(L),a,sep="\n")


# s = "10 11 21 19 21 17 21 16 21 18 15"
# l = s.split(" ")
# se = list(set(l))
# print(se)
# L = []
# d = {}
# for i in se:
#     d[s.count(i)] = i

# print(d)

from requests import options
from selenium import webdriver
from selenium.webdriver import ChromeOptions,ActionChains
from time import sleep

d = webdriver.Chrome()
d.get("https://pos.meituan.com/web/rms-account#/login")
d.maximize_window()
d.switch_to.frame(d.find_element_by_tag_name('iframe'))
d.find_element_by_xpath("//*[@id='app']/div/div[1]/a[2]").click()
d.find_element_by_id("account").send_keys("15882476647")
d.find_element_by_id("password").send_keys("yijian123789")
d.find_element_by_xpath("//*[@id='app']/div/div[2]/form/button").click()
sleep(1)

# # 添加参数
# options = ChromeOptions()
# # 事件参数对象
# actionChains = ActionChains(d)
# # 捕捉滑块元素
# slide_btn = d.find_elements_by_id("yodaBox")
# # 滑块长度和相对位置
# actionChains.drag_and_drop_by_offset(slide_btn,200,0).perform()

# d.close()