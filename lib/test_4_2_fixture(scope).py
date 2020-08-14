# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56

import pytest


@pytest.fixture(scope="module")  # ,autouse=True 自动激活？？
def open():
    print("打开浏览器，并且打开百度首页")

def test_s1(open):
    print("用例1：搜索python-1")

def test_s2(open):
    print("用例2：搜索python-2")

@pytest.mark.skip  # 自定义标签，跳过用例
def test_s3(open):
    print("用例3：搜索python-3")

@pytest.mark.xfail  # 预期失败的用例,此类用例执行结果会单独罗列出来
def test_s3(open):
    print("用例3：搜索python-3")

@pytest.mark.android  # 自定义标签,好像不太灵。。pytest test_mark.py -m=android   此命令只执行标签为android用例
def test_s3(open):
    print("用例3：搜索python-3")

if __name__ == "__main__":
    pytest.main(["-s", "test_f1.py"])