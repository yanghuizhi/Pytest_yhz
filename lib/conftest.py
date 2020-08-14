# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:58


import pytest

@pytest.fixture()
def login():
    print("输入账号，密码先登录")