# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/16 15:50


import requests
import urllib3
urllib3.disable_warnings()

def test_h():
    '''
    author: 上海-悠悠 QQ交流群：779429633
    blog: https://www.cnblogs.com/yoyoketang
    :return:
    '''
    url = "https://www.cnblogs.com/yoyoketang"
    s = requests.session()
    print(s)
    s.verify = False
    r = s.get(url)
    assert "牛" in r.text