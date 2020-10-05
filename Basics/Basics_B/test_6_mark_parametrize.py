# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56


import os

import pytest


# 参数化一
def add(a, b):
    return a + b


addList1 = [
    (1, 2, 3),
    (2, 2, 4),
    ('hi', ' wuya', 'hi wuya')
]


@pytest.mark.parametrize('a,b,result', addList1)
def test_add(a, b, result):
    assert add(a, b) == result


# 参数化二：使用 mark.parmmetrize
@pytest.mark.parametrize(
    "test_input,expected", [
        ("4+4", 8),
        ("5+5", 10),
        ("6 * 9", 42),
        pytest.param("6 * 9", 42, marks=pytest.mark.xfail)  # 标记单个用例失败
    ])
def test_2(test_input, expected):
    assert eval(test_input) == expected


if __name__ == "__main__":
    pytest.main(["-s", os.path.abspath(__file__)])


"""
命令、过程记录
pytest -sv "test_2_mark_1.py"

test_6_mark_parametrize.py::test_add[1-2-3] PASSED
test_6_mark_parametrize.py::test_add[2-2-4] PASSED
test_6_mark_parametrize.py::test_add[hi- wuya-hi wuya] PASSED
test_6_mark_parametrize.py::test_2[4+4-8] PASSED
test_6_mark_parametrize.py::test_2[5+5-10] PASSED
test_6_mark_parametrize.py::test_2[6 * 9-420] FAILED
test_6_mark_parametrize.py::test_2[6 * 9-421] XFAIL
"""
