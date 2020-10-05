# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/10/5 9:47

# 禁用xpass
# 设置xfail_strict = true可以让那些标记为@pytest.mark.xfail但实际通过的测试用例被报告为失败

import pytest

def test_hello():
    print("hello world!")
    assert 1

@pytest.mark.xfail()
def test_yoyo1():
    a = "hello"
    b = "hello world"
    assert a == b

@pytest.mark.xfail()
def test_yoyo2():
    a = "hello"
    b = "hello world"
    assert a != b

if __name__ == "__main__":
    pytest.main(["-v", "test_xpass.py"])

# 测试结果
# test_xpass.py::test_hello PASSED    [ 33%]
# test_xpass.py::test_yoyo1 xfail     [ 66%]
# test_xpass.py::test_yoyo2 XPASS     [100%]
# =============== 1 passed, 1 xfailed, 1 xpassed in 0.27 seconds ================
#
# test_yoyo1和test_yoyo2这2个用例一个是a == b一个是a != b,
# 两个都标记失败了，我们希望两个用例不用执行全部显示xfail。
# 实际上最后一个却显示xpass.为了让两个都显示xfail，那就加个配置
#
# xfail_strict = true
#
# # pytest.ini
# [pytest]
#
# markers =
#   webtest:  Run the webtest case
#   hello: Run the hello case
#
# xfail_strict = true
#
# 再次运行，结果就变成
#
# collecting ... collected 3 items
#
# test_xpass.py::test_hello PASSED        [ 33%]
# test_xpass.py::test_yoyo1 xfail         [ 66%]
# test_xpass.py::test_yoyo2 FAILED        [100%]
#
# ================================== FAILURES ===================================
# ================ 1 failed, 1 passed, 1 xfailed in 0.05 seconds ================
#
# 这样标记为xpasx的就被强制性变成failed的结果
