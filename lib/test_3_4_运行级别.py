# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 20:56

# 所有方法混合

# 1.如果一个.py的文件里面既有函数用例又有类和方法用例，运行顺序又是怎样的呢？


import pytest
# 类和方法


def setup_module():
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")

def teardown_module():
    print("teardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")

def setup_function():
    print("setup_function：每个用例开始前都会执行")

def teardown_function():
    print("teardown_function：每个用例结束前都会执行")

def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x

def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'check')

class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def test_three(self):
        print("正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行----test_four")
        x = "hello"
        assert hasattr(x, 'check')

if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])


"""
setup_module：整个.py模块只执行一次
比如：所有用例开始前只打开一次浏览器
setup_function：每个用例开始前都会执行
正在执行----test_one
.teardown_function：每个用例结束前都会执行
setup_function：每个用例开始前都会执行
正在执行----test_two
Fteardown_function：每个用例结束前都会执行
setup_class：所有用例执行之前
正在执行----test_three
.正在执行----test_four
Fteardown_class：所有用例执行之前
teardown_module：整个.py模块只执行一次
比如：所有用例结束只最后关闭浏览器



2.从运行结果看出，
setup_module/teardown_module的优先级是最大的，
然后函数里面用到的setup_function/teardown_function与类里面的setup_class/teardown_class互不干涉
"""