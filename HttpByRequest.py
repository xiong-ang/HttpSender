import requests
from bs4 import BeautifulSoup
import ssl 
ssl._create_default_https_context = ssl._create_unverified_context  

url="https://passport.csdn.net/account/login?ref=toolbar"

#登陆前准备：获取lt和exection
s = requests.Session()
response = s.get(url,verify=False)
soup = BeautifulSoup(response.text)
for input in  soup.form.find_all("input"):
    if input.get("name") == "lt":
        lt = input.get("value")
    if input.get("name") == "execution":
        execution = input.get("value")

#http请求头
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}

#post信息
values = {
        "username":"287223609@qq.com",
        "password":"***",
        "lt":lt,
        "execution":execution,
        "_eventId":"submit"
    }

#登录
r = s.post(url, data = values, headers=headers,verify=False)

#用登录的session访问其他网站
url = "http://my.csdn.net/my/mycsdn"
html=s.get(url,headers=headers,cookies=r.cookies,verify=False)

#保持稳健
file_object = open('thefile.html', 'w',encoding="utf-8")
file_object.write(html.text)
file_object.close( )
print("Finish~")