# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 20:56

# 用例运行级别
#
# 模块级（setup_module/teardown_module）开始于模块始末，全局的（不在类中,就算在类中也不会生效）
# 函数级（setup_function/teardown_function）只对函数用例生效（不在类中，就算在类中也不会生效）
# TODO 类里面的（setup/teardown）运行在调用方法的前后（类中类外看起来都可以）
# TODO 类级（setup_class/teardown_class）只在类中前后运行一次(在类中)
# TODO 方法级（setup_method/teardown_method）开始于方法始末（在类中）

import pytest
import os


class TestCase:

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
        print("第一条测试用例正在执行")
        assert 'h' in "this"

    def test_two(self):
        print("第二条测试用例正在执行")
        assert 'h' in "this"


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])

"""
setup_class：所有用例执行之前

    setup_method:  每个用例开始前执行
        setup: 每个用例开始前执行
            第一条测试用例正在执行
        teardown: 每个用例结束后执行
    teardown_method:  每个用例结束后执行
    
    setup_method:  每个用例开始前执行
        setup: 每个用例开始前执行
            第二条测试用例正在执行
        teardown: 每个用例结束后执行
    teardown_method:  每个用例结束后执行
    
teardown_class：所有用例执行之前
"""