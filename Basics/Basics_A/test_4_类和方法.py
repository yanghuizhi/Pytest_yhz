# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 20:56

# 所有方法混合
# 模块级（setup_module/teardown_module）开始于模块始末，全局的（不在类中,就算在类中也不会生效）
# 函数级（setup_function/teardown_function）只对函数用例生效（不在类中，就算在类中也不会生效）
# 类里面的（setup/teardown）运行在调用方法的前后（类中类外看起来都可以）
# 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
# 方法级（setup_method/teardown_method）开始于方法始末（在类中）


import pytest
import os


def setup():
    print("setup: 每个用例开始前执行，类外面")


def teardown():
    print("teardown: 每个用例结束后执行。类外面")


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
    print("第一个测试用例")
    assert 'h' in "this"


def test_two():
    print("第二个测试用例")


class TestCase:

    def setup(self):
        print("setup: 每个用例开始前执行，类里面")

    def teardown(self):
        print("teardown: 每个用例结束后执行，类里面")

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def setup_method(self):
        print("setup_method:  每个用例开始前执行")

    def teardown_method(self):
        print("teardown_method:  每个用例结束后执行")

    def test_3(self):
        print("第3条测试用例正在执行")
        assert 'h' in "this"

    def test_4(self):
        print("第4条测试用例正在执行")
        assert 'h' in "this"


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])

"""
setup_module：整个.py模块只执行一次
比如：所有用例开始前只打开一次浏览器
    setup_function：每个用例开始前都会执行
        setup: 每个用例开始前执行，类外面
            第一个测试用例
        teardown: 每个用例结束后执行。类外面
    teardown_function：每个用例结束前都会执行
    setup_function：每个用例开始前都会执行
        setup: 每个用例开始前执行，类外面
            第二个测试用例
        teardown: 每个用例结束后执行。类外面
    teardown_function：每个用例结束前都会执行
    setup_class：所有用例执行之前
        setup_method:  每个用例开始前执行
            setup: 每个用例开始前执行，类里面
                第3条测试用例正在执行
            teardown: 每个用例结束后执行，类里面
        teardown_method:  每个用例结束后执行
        setup_method:  每个用例开始前执行
            setup: 每个用例开始前执行，类里面
                第4条测试用例正在执行
            teardown: 每个用例结束后执行，类里面
        teardown_method:  每个用例结束后执行
    teardown_class：所有用例执行之前
teardown_module：整个.py模块只执行一次
比如：所有用例结束只最后关闭浏览器
"""
