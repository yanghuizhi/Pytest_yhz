# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:58

# Pytest中使用conftest.py来共享fixture，该文件不可导入
import pytest

@pytest.fixture()
def login():
    print("输入账号，密码先登录")

# hook调用