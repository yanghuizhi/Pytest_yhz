# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 20:56
import pytest
from _GlobalConfig import *


class Test_Class(object):

    def test_1(self):
        assert 'yhz' in "yang"

    def test_2(self):
        return "yanghuizhi"

    def test_3(self):
        a = "hello"
        b = "hello world"
        assert a in b


if __name__ == '__main__':
    # The default read pytest.ini
    path = os.path.abspath(__file__)
    pytest.main([PATH_6])


"""
在运行的时候，也可以指定参数运行
-s：显示程序中的 print/logging 输出
-v: 丰富信息模式, 输出更详细的用例执行信息
-k：运行包含某个字符串的测试用例。如：pytest -k add XX.py 表示运行 XX.py 中包含 add 的测试用例。
-q: 简单输出模式, 不输出环境信息
-x: 出现一条测试用例失败就退出测试。在调试阶段非常有用，当测试用例失败时，应该先调试通过，而不是继续执行测试用例。
# 当前走配置，即pytest.ini
"""