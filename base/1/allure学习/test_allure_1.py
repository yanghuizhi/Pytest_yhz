# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/16 14:25
import allure
import pytest


@allure.description("描述动态更新：失败时展示这里的内容")
def test_1():
    assert 1 == int(1 * 2)
    allure.dynamic.description("描述动态更新：成功时展示这里的内容")


@allure.description("描述动态更新：失败时展示这里的内容")
def test_2():
    assert 2 == int(1 * 2)
    allure.dynamic.description("描述动态更新：成功时展示这里的内容")


@allure.title("标题动态更新：失败时展示这里的内容")
def test_3():
    assert 1 == int(1 * 2)
    allure.dynamic.title('标题动态更新：成功时展示这里的内容')


@allure.title("标题动态更新：失败时展示这里的内容")
def test_4():
    assert 2 == int(1 * 2)
    allure.dynamic.title('标题动态更新：成功时展示这里的内容')
