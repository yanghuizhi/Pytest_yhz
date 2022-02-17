# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56
import os
import pytest


@pytest.fixture()
def open():
    print("打开浏览器，并且打开百度首页")


@pytest.mark.skip  # 自定义标签：跳过用例
def test_1(open):
    print("用例一")


@pytest.mark.fail  # 预期失败的用例,此类用例执行结果会单独罗列出来
def test_2(open):
    print("用例二")


@pytest.mark.android  # 自定义标签
def test_3(open):
    print("用例三：pytest test_mark.py -m=android")


@pytest.mark.ios  # 自定义标签
def test_4(open):
    print("用例四：pytest test_mark.py -m=android")


@pytest.mark.android
@pytest.mark.ios
def test_5(open):
    print("用例五")


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])


"""
标准标签：
    @pytest.mark.skip   跳过用例
        @pytest.mark.skip(reason='忽略执行该测试用例'),使用命令pytest -rs，可显示出忽略的详细信息
    @pytest.mark.fail   预计失败用例
    @pytest.mark.repeat(count)  重复用例执行次数

自定义标签：
    执行方法： pytest.main(['-s', 'mark_02.py', "-m='not webtest'"])
              pytest -s test_2_mark.py -m=ios

通过这一章的，我知道了：
    1、可以使用标准标签来进行标记
    2、可以使用 mark 来进行自定义标签，使用-m指定使用的用例
    3、可以多个标签对应同一个用例，最简单的就是对系统的区分
遗留问题：
    1、运行后会有警告，说自定义标签没有注册，这块暂时留下来
"""
