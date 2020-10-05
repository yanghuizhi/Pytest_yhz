# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56

import os
import pytest


@pytest.fixture(scope="module")
def open():
    print("打开浏览器，并且打开百度首页")
    yield
    print("执行teardown!")
    print("最后关闭浏览器")


def test_1(open):
    print("用例1...")


def test_2(open):
    print("用例2...")
    raise NameError  # 模拟异常


def test_3(open):
    print("用例3...")


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])


"""
1.如果其中一个用例出现异常，不影响yield后面的teardown执行,运行结果互不影响，
并且全部用例执行完之后，yield呼唤teardown操作


打开浏览器，并且打开百度首页
    用例1...
    用例2...
    F.用例3...
执行teardown!
最后关闭浏览器


"""