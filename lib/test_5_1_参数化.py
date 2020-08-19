# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56

import pytest
@pytest.mark.parametrize("test_input,expected",
                         [ ("3+5", 8),
                           ("2+4", 6),
                           ("6 * 9", 42),
                         ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

if __name__ == "__main__":
    pytest.main(["-s", "test_canshu1.py"])


"""
def add(a,b):
    return a+b

addList1=[
    (1,2,3),
    (2,2,4),
    ('hi',' wuya','hi wuya')
]

@pytest.mark.parametrize('a,b,result',addList1)
def test_add(a,b,result):
    assert  add(a,b)==result

"""