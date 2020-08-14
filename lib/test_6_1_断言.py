# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56

import pytest
@pytest.mark.web_test
def f():
    return 3

@pytest.mark.app_test   # 练习pytest.ini 随手加的
def test_function():

    a = f()
    assert a % 2 == 0, "判断a为偶数，当前a的值为：%s"%a