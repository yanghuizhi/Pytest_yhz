# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 20:56

# 用例运行级别
#
# 模块级（setup_module/teardown_module）开始于模块始末，全局的
# 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）
# 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
# 方法级（setup_method/teardown_method）开始于方法始末（在类中）
# 类里面的（setup/teardown）运行在调用方法的前后

import pytest
# 函数式


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

def test_three():
    print("正在执行----test_three")
    a = "hello"
    b = "hello world"
    assert a in b

if __name__ == "__main__":
    pytest.main(["-s", "test_fixt.py"])

"""
setup_module：整个.py模块只执行一次
比如：所有用例开始前只打开一次浏览器
setup_function：每个用例开始前都会执行
正在执行----test_one
.teardown_function：每个用例结束前都会执行
setup_function：每个用例开始前都会执行
正在执行----test_two
Fteardown_function：每个用例结束前都会执行
setup_function：每个用例开始前都会执行
正在执行----test_three
.teardown_function：每个用例结束前都会执行
teardown_module：整个.py模块只执行一次
比如：所有用例结束只最后关闭浏览器


setup_function/teardown_function和setup_module/teardown_module这四种方法是可以任意组合的，用一个和多个都可以
每个用例执行前都会执行 function方法
整个py模块中只执行一次module 方法
"""