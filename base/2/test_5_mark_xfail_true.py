# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56


import pytest

canshu = [{"user": "amdin", "psw": "12345"}]


@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    print("正在操作登录，账号：%s, 密码：%s" % (user, psw))
    if psw:
        return True
    else:
        return False


@pytest.mark.parametrize("login", canshu, indirect=True)
class Test_xx:

    def test_01(self, login):
        """用例1登录"""
        result = login
        print("用例1,登录结果：%s" % result)
        assert result == True

    def test_02(self, login):
        result = login
        print("用例2,登录结果：%s" % result)
        if not result:
            pytest.xfail("登录不成功, 标记为xfail")

        assert 1 == 1

    def test_03(self, login):
        result = login
        print("用例3,登录结果：%s" % result)
        if not result:
            pytest.xfail("登录不成功, 标记为xfail")

        assert 1 == 1


if __name__ == "__main__":
    pytest.main(["-s", "test_05.py"])

"""
正在操作登录，账号：amdin, 密码：12345
    用例1,登录结果：True
    用例2,登录结果：True
    用例3,登录结果：True
"""
