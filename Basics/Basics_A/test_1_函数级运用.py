# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 20:56

# 用例运行级别
#
# 模块级（setup_module/teardown_module）开始于模块始末，全局的（不在类中）
# 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
# 方法级（setup_method/teardown_method）开始于方法始末（在类中）
# 类里面的（setup/teardown）运行在调用方法的前后（类中类外看起来都可以）
# TODO 函数级（setup_function/teardown_function）只对函数用例生效（不在类中）


import os
import pytest


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束后都会执行")


def test_one():
    print("第一个测试用例")


def test_two():
    print("第二个测试用例")


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])


"""
setup_function：每个用例开始前都会执行
    第一个测试用例
teardown_function：每个用例结束后都会执行
setup_function：每个用例开始前都会执行
    第二个测试用例
teardown_function：每个用例结束后都会执行
"""
