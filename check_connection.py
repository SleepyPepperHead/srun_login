from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import datetime, time
from bs4 import BeautifulSoup
import requests


def check_connection():
    baidu_request = requests.get('http://www.baidu.com')
    if (baidu_request.status_code == 200):
        baidu_request.encoding = 'utf-8'
        baidu_request_bsObj = BeautifulSoup(baidu_request.text, 'html.parser')
        baidu_input = baidu_request_bsObj.find(value="百度一下")
        if baidu_input == None:
            return False
        return True

username_str = '3001190001' # 你的校园网登陆用户名
password_str = '54181452' # 你的校园网登陆密码

can_connect = True

def login():
    try:
        options = Options()
        options.add_argument("--headless")
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Firefox(executable_path=r"geckodriver.exe", options=options)

        driver.get("http://gw.cugb.edu.cn/srun_portal_pc?ac_id=1&theme=default") # 你的校园网登陆地址
        time.sleep(3)
        username_input = driver.find_element_by_id("username") # 校园网登陆用户名的输入控件ID, 浏览器上右键查看网页源代码查询
        password_input = driver.find_element_by_id("password") # 校园网登陆密码的输入控件ID, 浏览器上右键查看网页源代码查询
        print('Searching connect')
        login_button = driver.find_element_by_id("login") # 校园网登陆连接的点击控件ID, 浏览器上右键查看网页源代码查询
        print('Find connect successfully')
        username_input.send_keys(username_str)
        password_input.send_keys(password_str)
        print('Input user info')
        login_button.click()
        print('Connected')
    except:
        print(u"login ERROR !!!!")
    finally:
        driver.close()

while True:
    if check_connection():
        print('online', datetime.datetime.now(), )
    else:
        print('offline, try to login...')
        login()

    time.sleep(60)
