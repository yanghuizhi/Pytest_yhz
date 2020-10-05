# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56

import pytest


@pytest.mark.parametrize("x", [0, 1, 2])
@pytest.mark.parametrize("y", [2, 3])
def test_foo(x, y):
    print("测试数据组合：x->%s, y->%s" % (x, y))


if __name__ == "__main__":
    pytest.main(["-s", "test_canshu1.py"])

"""
参数化组合

测试数据组合：x->0, y->2
测试数据组合：x->1, y->2
测试数据组合：x->2, y->2
测试数据组合：x->0, y->3
测试数据组合：x->1, y->3
测试数据组合：x->2, y->3
"""