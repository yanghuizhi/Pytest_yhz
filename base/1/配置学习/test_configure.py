# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/10/3 20:34
import os
import pytest


def test_1():
    print("test_1")
    a = "hello"
    b = "helloo"
    assert a == b


def test_2(conf):
    print("test_2")


def test_3():
    print("test_3")
    a = "hello"
    b = "hello"
    assert a == b


if __name__ == "__main__":
    pytest.main(["-s", "-v", os.path.abspath(__file__)])


"""
这里是配置文件
    用例1...
    用例2...
这里是配置文件
    用例3...
"""