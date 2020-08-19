# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56

import pytest

# 固定装置 & 测试夹具
# 不带参数时默认scope="function"
# @pytest.fixture()
# def login():
#     print("输入账号，密码先登录")

def test_s1(login):
    print("用例1：登录之后其它动作111")

def test_s2():  # 不传login
    print("用例2：不需要登录，操作222")

def test_s3(login):
    print("用例3：登录之后其它动作333")

if __name__ == "__main__":
    pytest.main(["-s", "test_fix.py"])

"""
6. 使用fixture执行配置及销毁逻辑

做测试前后的初始化设置，如测试数据准备，链接数据库，打开浏览器等这些操作都可以使用fixture来实现

这样在执行每个测试用例之前，先执行login函数

可以将fixture写入conftest.py，这样当前路径下所有的所有用例可以使用conftest.py文件（不需要导入，可以跨文件共享）

Fixture里面有个scope参数，可以控制fixture的范围：session>module>class>function

Function（函数级）: 每一个函数活方法都会被调用
Class（类级）：     每一个类调用一次，一个类可以有多个方法
Module（模块级）：  每个.py文件调用一次，该文件内有多个function和class
Session（会话级）： 是多个文件调用一次，可以跨.py文件调用，每个.py文件就是module
package（包级）：   包级，载入每个包前，均会重新生成 fixture

params：可选多个参数调用fixture
autouse：如果是True，则为所有测试激活fixture，如果是false，则需要显示激活
ids：每个字符串ID的列表，每个字符串对应于param，这是测试ID的一部分
name：fixture的名称
"""