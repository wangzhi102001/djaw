# coding:utf-8
# include <sys.stdin>
# include <sys.stdout>
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
import time
import urllib
import urllib3

import file_transport as e_to_j
import carData
import setting
import json
import sys
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime
import pytesser3 as pyt3
from PIL import Image
from io import BytesIO




# 读取json数据库,获取待处理列表
list_car_js = []  # 所有待处理的贫困户数据JS类型
list_car = []  # 所有待处理的贫困户数据
carDatas = []
n = 0  # 计数器
end = 0
start = 0
error = 0
switch_1 = True
error_count = 0
time_clock = 5
b = True
my = setting.setting("ctsz","123456")
#大型汽车=大型汽车
#低速车 =？无法提取
#普通摩托车=？无法提取
#轻便摩托车=？无法提取
#拖拉机=？无法提取


#while True:
    
#    if input_num == "1":
#        my.get_and_save_setting()#

#e_to_j.excel_json('car.xlsx' or 'car.xls', 'car.json')
#input()
#e_to_j.file_to_json_fomat(
#"car.json", "car2.json",  list_car)
## e_to_j.json_to_personDatalist("002.json",list_poor_family_js,list_poor_family,error,start,end,n)
#input("数据转换完成，生成文件完成，程序即将关闭，下次使用请输入2，按任意键退出......")
#sys.exit()

#    elif input_num == "2":
#my.load_setting()
#start = time.time()

e_to_j.json_to_carDatalist(
    "car2.json", list_car_js, list_car, error, start, end, n,1,5000)#读取11767条数据耗时13秒
print(list_car[1].hpzl)


#e_to_j.carDatalist_to_json(list_car, 'car2.json')

#input()
#end = time.time()
#print (end-start)
#input()
#start = time.time()
#e_to_j.carDatalist_to_json(list_car, 'car2.json')#写入11767条数据耗时13秒
#end = time.time()
#print (end-start)


#    elif input_num == "3":
#        e_to_j.js_to_xlsx('002.json', 'error.xlsx')
#        # 将002.json中error=true的项提取出来并写入error+datetime.excel
#        input("按任意键退出......")
#        sys.exit()
#    else:
#        print("请重新输入")
## input()

#e_to_j.personDatalist_to_json(list_poor_family, '002.json')

## 初始化---------
## input()
## e_to_j.save_as_json(list_poor_family,'002.json')

## 构造模拟浏览器


chromedriver = my.chromePath

os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
driver.implicitly_wait(5)




url = my.url
#----------------------------------------------------------------开始录入车辆------------------------------------
driver.get(url)  # 打开网址
driver.maximize_window()  # 窗口最大化

time.sleep(2)


driver.find_element_by_xpath(my.xpath1).send_keys(my.account)  # 输入账号
# time.sleep(1)
driver.find_element_by_xpath(my.xpath2).send_keys(my.password)  # 输入密码
driver.find_element_by_xpath(my.xpathyzmflash).click()  # 点击刷新验证码

yanzhengma = input("请手动输入验证码：")
driver.find_element_by_xpath(my.xpath3).send_keys(yanzhengma)  # 输入验证码
driver.find_element_by_xpath(my.xpath4).click()  # 点击登陆

#yanzhengma = pyt3.image_file_to_string('code.png')[:4]

# 验证码处理
#while b:
#    driver.find_element_by_xpath(
#        my.xpathyzmflash).click()  # 点击刷新验证码
#    time.sleep(1)
#    driver.save_screenshot('screenshot.png')
#    imgelement = driver.find_element_by_id('yzmImage')
#    location = imgelement.location  # 获取验证码x,y轴坐标
#    size = imgelement.size  # 获取验证码的长宽
#    rangle = (int(location['x']), int(location['y']), int(
#        location['x']+size['width']), int(location['y']+size['height']))  # 写成我们需要截取的位置坐标
#    i = Image.open("screenshot.png")  # 打开截图
#    result = i.crop(rangle)  # 使用Image的crop函数，从截图中再次截取我们需要的区域
#    result.save('result.png')
#    yanzhengma = pyt3.image_file_to_string('result.png', 'eng').replace(' ','')[:4]
#    print(">%s<" % yanzhengma)
#    driver.find_element_by_xpath(my.xpath3).clear() #清空验证码输入栏
#    driver.find_element_by_xpath(my.xpath3).send_keys(yanzhengma)  # 输入验证码
#    driver.find_element_by_xpath(my.xpath4).click()  # 点击登陆
#    time.sleep(2)

#    input()
    # 登陆成功
    #try:
    #    driver.find_element_by_xpath(
    #        "//div[contains(text(),'验证码不正确,请重新输入验证码')]")
    #    time.sleep(1)
    #    driver.find_element_by_xpath(
    #        "//button[@class = 'swal2-confirm swal2-styled']").click()
    #except:
    #    b = False


# 加载时间过长 异常处理
time.sleep(2)
driver.switch_to_frame('leftFrame') #切换iframe
#driver.find_element_by_xpath(my.xpath102).click() #点击农村驾驶人
time.sleep(1)
driver.find_element_by_xpath(my.xpath5).click()

#js = "document.querySelector('#menutab_2').click()"
#driver.execute_script(js)

#driver.find_element_by_xpath(my.xpath5).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpathjcxxgl).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpath7).click()
time.sleep(1)
driver.find_element_by_xpath(my.xpath8).click()
time.sleep(1)
driver.switch_to.default_content() #恢复默认表单
driver.switch_to_frame('rightFrame') #切换iframe

main_windows=driver.current_window_handle #标记当前窗口为主窗口
driver.find_element_by_xpath(my.xpath9).click()  
#time.sleep(2)
all_handles=driver.window_handles#标记所有窗口

for handle in all_handles:
    if handle !=main_windows:
        driver.switch_to_window(handle)#切换到非主窗口

# "大型汽车", "J7D220", "重型普通货车",  "货运",  "13777761839",  "车溪乡翊武村民委员会8组08046号",  "城头山镇",  "",  "","1" 
#   "大型汽车""J78783","中型自卸货车", "货运", "18573635693","车溪乡万兴村2组02029号",  "城头山镇", "",  "","2"
#list_car=[carData.carData("大型汽车","J78783","中型自卸货车", "货运", "18573635693","车溪乡万兴村2组02029号",  "城头山镇", "",  "","2"),carData.carData("大型汽车","J7D220", "重型普通货车",  "货运",  "13777761839",  "车溪乡翊武村民委员会8组08046号",  "城头山镇",  "",  "","1" )]



    # for p1 in list(reversed(list_poor_family[:])):
for p1 in list_car:
    #if p1.suoyin.endswith("50"):#每隔50条保存一次
    #        e_to_j.carDatalist_to_json(list_car, 'car.json')
    

    if (p1.edit == False and p1.error == False): 
        if p1.suoyin.endswith("0"):#每隔50条保存一次
            e_to_j.carDatalist_to_json(list_car, 'car2.json')#写入11767条数据耗时13秒
        time.sleep(1)
        ele = driver.find_element_by_xpath(my.xpath11)  
        driver.execute_script("arguments[0].focus();",ele)
        time.sleep(1)
        driver.find_element_by_xpath(my.xpath10).click()  # 点击获取行政区划
        time.sleep(0.5)
        driver.find_element_by_xpath(my.xpathHPZL).find_element_by_xpath("//option[@attname='%s']"% p1.hpzl).click()  # 点击获取号牌种类

        time.sleep(0.5)
        driver.find_element_by_xpath(my.xpathHPHM).clear() #清空
        if p1.hpzl =="拖拉机":
            driver.find_element_by_xpath(my.xpathHPHM).send_keys(p1.carnumber[1:]) #输入号牌
        else:
            driver.find_element_by_xpath(my.xpathHPHM).send_keys(p1.carnumber) #输入号牌
        time.sleep(1)
        driver.find_element_by_xpath(my.xpath16).click()  # 点击查重
        time.sleep(1)
        if '勿重复录入' in driver.find_element_by_xpath(my.xpath19).text:
            driver.find_element_by_xpath(my.xpath18).click() #点击确定
            p1.pass_state()
            continue
        else:
            driver.find_element_by_xpath(my.xpath18).click() #点击确定
        time.sleep(1)
        #ele2 = driver.find_element_by_xpath(my.xpath15)
        #driver.execute_script("arguments[0].click();",ele)# 点击提取

        driver.find_element_by_xpath(my.xpath15).click()  # 点击提取
        time.sleep(2)        
        driver.find_element_by_xpath(my.xpath18).click()  # 点击提取后弹窗确定

        time.sleep(1)
        if p1.hpzl=='大型汽车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//option[@attname='蓝牌货车']").click()  # 点击获取车辆类别
        elif p1.cllx=='自卸低速货车'or p1.cllx=='普通低速货车'or p1.cllx=='罐式低速货车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//select[@id='CheLLB']/option[@attname='三轮汽车']").click()  # 点击获取车辆类别
        elif p1.cllx=='三轮汽车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//select[@id='CheLLB']/option[@attname='三轮汽车']").click()  # 点击获取车辆类别
        elif p1.cllx=='普通二轮摩托车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//select[@id='CheLLB']/option[@attname='两轮摩托车']").click()  # 点击获取车辆类别
        elif p1.cllx=='普通正三轮摩托车'or p1.cllx=='正三轮载货摩托车'or p1.cllx=='正三轮载客摩托车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//select[@id='CheLLB']/option[@attname='三轮摩托车']").click()  # 点击获取车辆类别
        elif p1.cllx=='轻便二轮摩托车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//select[@id='CheLLB']/option[@attname='两轮摩托车']").click()  # 点击获取车辆类别
        elif p1.cllx=='小型方向盘式拖拉机' or p1.cllx=='大中型拖拉机':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//option[@attname='拖拉机（农用车）']").click()  # 点击获取车辆类别

        elif p1.cllx=='轻型仓栅式货车' or p1.cllx=='轻型封闭货车' or p1.cllx=='轻型普通货车' or p1.cllx=='轻型厢式货车' or p1.cllx=='轻型自卸货车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//option[@attname='黄牌货车']").click()  # 点击获取车辆类别
        elif p1.cllx=='微型轿车'or p1.cllx=='小型轿车'or p1.cllx=='小型面包车' or p1.cllx == '小型普通客车' or p1.cllx == '小型越野客车' or p1.cllx == '小型专用客车':
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//option[@attname='小客车（轿车）']").click()  # 点击获取车辆类别
        else :
            driver.find_element_by_xpath(my.xpathCLLB).find_element_by_xpath("//option[@attname='其他']").click()  # 点击获取车辆类别

        time.sleep(1)

        if p1.hpzl =="拖拉机":
            driver.find_element_by_xpath(my.xpathSYXZ).find_element_by_xpath("//option[@attname='非营运']").click()  # 点击获取使用性质
        elif p1.syxz =="非营运":
            driver.find_element_by_xpath(my.xpathSYXZ).find_element_by_xpath("//option[@attname='非营运']").click()  # 点击获取使用性质
        elif p1.syxz =="货运":
            driver.find_element_by_xpath(my.xpathSYXZ).find_element_by_xpath("//option[@attname='货运']").click()  # 点击获取使用性质
        elif p1.syxz =="营转非":
            driver.find_element_by_xpath(my.xpathSYXZ).find_element_by_xpath("//option[@attname='营转非']").click()  # 点击获取使用性质
        else:
            driver.find_element_by_xpath(my.xpathSYXZ).find_element_by_xpath("//option[@attname='其他']").click()  # 点击获取使用性质
        time.sleep(1)

        driver.find_element_by_xpath(my.xpath25).click()  #是否客运车辆 否 radio按钮
        time.sleep(1)
        driver.find_element_by_xpath(my.xpath24).send_keys(p1.date)#传入摸底日期
        driver.find_element_by_xpath(my.xpath20).click()#点击保存
        p1.show_edit()
        time.sleep(1)
        driver.find_element_by_xpath(my.xpath18).click()#点击继续
    else :
        p1.pass_state()


driver.switch_to_window(main_windows)#切换到主窗口
with open("log.txt", 'w', encoding="utf-8") as f:
    for p1 in list_car:
        f.writelines(p1.log+'\n')
driver.close()

