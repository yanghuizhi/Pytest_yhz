# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/10 15:27


#导包
import requests
#定义一个url
url = "http://xxxxxxx"
#传递参数
payload="{\"head\":{\"accessToken\":\"\",\"lastnotice\":0,\"msgid\":\"\"},\"body\":{\"user_name\":\"super_admin\",\"password\":\"b50c34503a97e7d0d44c38f72d2e91ad\",\"role_type\":1}}"
headers = {
  'Content-Type': 'text/plain',
  'Cookie': 'akpsysessionid=bafc0ad457d5a99f3a4e53a1d4b32519'
}
#发送get请求
r = requests.get( url=url,headers=headers, data=payload)
#打印结果
print(r.text)
#解码
print(r.encoding)
print(r.text.encode('utf-8').decode('unicode_escape'))#先把返回的结果转换成utf-8，再去解码成中文的编码