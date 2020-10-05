# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/10/4 13:47


# 配置文件pytest.ini

"""
前言
    pytest里面有些文件是非test文件
        pytest_1.ini pytest的主配置文件，可以改变pytest的默认行为
        conftest.py 测试用例的一些fixture配置
        _init_.py 识别该文件夹为python的package包
        tox.ini 与pytest.ini类似，用tox工具时候才有用
        setup.cfg 也是ini格式文件，影响setup.py的行为

使用pytest —-help指令可以查看pytest.ini的设置选项
使用pytest —-markers指令可以查看 mark标记
"""

