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
# 类和方法


class TestCase():

    def setup(self):
        print("setup: 每个用例开始前执行")

    def teardown(self):
        print("teardown: 每个用例结束后执行")

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def test_one(self):
        print("正在执行----test_one")
        x = "this"
        assert 'h' in x

    def test_two(self):
        print("正在执行----test_two")
        x = "hello"
        assert hasattr(x, 'check')

    def test_three(self):
        print("正在执行----test_three")
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])

"""
setup_class：所有用例执行之前
setup_method:  每个用例开始前执行
setup: 每个用例开始前执行
正在执行----test_one
.teardown: 每个用例结束后执行
teardown_method:  每个用例结束后执行
setup_method:  每个用例开始前执行
setup: 每个用例开始前执行
正在执行----test_two
Fteardown: 每个用例结束后执行
teardown_method:  每个用例结束后执行
setup_method:  每个用例开始前执行
setup: 每个用例开始前执行
正在执行----test_three
.teardown: 每个用例结束后执行
teardown_method:  每个用例结束后执行
teardown_class：所有用例执行之前



setup_class》setup_method》setup 》用例》teardown》teardown_method》teardown_class

备注：这里setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可

每个用例执行前都会执行 function方法，在类里面不管用，的用 setup方法
整个py模块中只执行一次module 方法
class是最大的
"""