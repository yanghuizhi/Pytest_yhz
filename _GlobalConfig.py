# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:58

"""
pytest 会默认读取 _GlobalConfig.py 里面的所有 fixture，无需手动导入
_GlobalConfig.py 文件名称是固定的，不能改动
_GlobalConfig.py 只对同一个 package 下的所有测试用例生效
    不同目录可以有自己的conftest.py，一个项目中可以有多个conftest.py
"""

import os
import time

PATH = os.path.abspath(os.path.join(os.getcwd(), "../.."))
PATH_1 = os.getcwd()
PATH_2 = os.path.join(os.getcwd(), "base")
PATH_3 = os.path.join(os.getcwd(), "base", "1")
PATH_4 = os.path.join(os.getcwd(), "base", "2")
PATH_5 = os.path.join(os.getcwd(), "base", "3")
PATH_6 = os.path.join(os.getcwd(), "base", "Basics_B")
report = os.path.join(os.getcwd(), "report")
allure_report = os.path.join(os.getcwd(), "report", "allure-report")
allure_result = os.path.join(os.getcwd(), "report", "allure_result")

DATE = time.strftime("%Y%m%d")
DATE_2 = time.strftime("%Y%m%d%H%M%S")
