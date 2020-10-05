# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:58、

# Pytest中使用conftest.py来共享fixture，该文件不可导入
# 放到工程的根目录下，可以全局调用，如果放到某个package包下，那就只在该package内有效

import pytest


@pytest.fixture()
def conf():
    print("这里是配置文件")

