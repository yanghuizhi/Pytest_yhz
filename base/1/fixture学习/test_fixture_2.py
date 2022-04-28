# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/20 10:52

import pytest
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/

def delete_sql(user):
    '''这里执行SQL'''
    sql = "delete from auth_user WHERE username = '%s';"%user
    print("执行的sql:%s"%sql)
    # 调用执行SQL的封装函数

# 测试数据，存放在list
user_data = ["user1", "user2"]

@pytest.fixture(scope="function", params=user_data)
def users(request):
    '''注册用户参数化'''

    # 前置操作
    delete_sql(request.param)

    yield request.param

    # # 后置操作
    # delete_sql(request.param)

def test_register(users):
    print("注册用户：%s"%users)

if __name__ == '__main__':
    pytest.main(["-s", "test_fixture_params.py"])