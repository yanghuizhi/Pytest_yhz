# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/20 10:51


# request 是pytest的内置 fixture ，主要用于传递参数
# test_fixture_params.py
import pytest
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/

# 测试数据，存放在list
user_data = ["user1", "user2"]

@pytest.fixture(scope="function", params=user_data)
def users(request):
    '''注册用户参数化'''
    return request.param

def test_register(users):
    print("注册用户：%s"%users)

if __name__ == '__main__':
    pytest.main(["-s", "test_fixture_params"])