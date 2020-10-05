# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/10/3 20:34
import os
import pytest


def test_1(conf):
    print("用例1...")


def test_2():
    print("用例2...")


def test_3(conf):
    print("用例3...")


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])


"""
这里是配置文件
    用例1...
    用例2...
这里是配置文件
    用例3...
"""