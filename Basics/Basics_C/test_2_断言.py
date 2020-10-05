# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56

import pytest

# 常用断言
#
# pytest里面断言实际上就是python里面的assert断言方法，常用的有以下几种
#   assert  xx  判断xx为真
#   assert not xx 判断xx不为真
#   assert a in b  判断b包含a
#   assert a == b 判断a等于b
#   assert a != b  判断a不等于b


def is_true(a):
    if a > 0:
        return True
    else:
        return False


def test_01():
    """断言xx为真"""
    a = 5
    b = -1
    assert is_true(a)
    assert not is_true(b)  # 一个用例可以支持多个断言


def test_02():
    """断言b 包含 a"""
    a = "hello"
    b = "hello world"
    assert a in b


def test_03():
    """断言相等"""
    a = "yoyo"
    b = "yoyo"
    assert a == b


def test_04():
    """断言不等于"""
    a = 5
    b = 6
    assert a != b


if __name__ == "__main__":
    pytest.main(["-s", "test_01.py"])


"""
test_2_断言.py::test_01 PASSED
test_2_断言.py::test_02 PASSED
test_2_断言.py::test_03 PASSED
test_2_断言.py::test_04 PASSED
"""