# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:58
import pytest

"""
pytest 会默认读取 conftest.py 里面的所有 fixture，无需手动导入
conftest.py 文件名称是固定的，不能改动
conftest.py 只对同一个 package 下的所有测试用例生效
    不同目录可以有自己的conftest.py，一个项目中可以有多个conftest.py
"""


@pytest.fixture()
def conf():
    print("这里是配置文件")

