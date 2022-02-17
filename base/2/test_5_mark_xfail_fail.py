# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yhz
# Time: 2020/7/31 21:56


"""
标记失败xfail

前言

当用例a失败的时候，如果用例b和用例c都是依赖于第一个用例的结果，那可以直接跳过用例b和c的测试，直接给他标记失败xfail

用到的场景，登录是第一个用例，登录之后的操作b是第二个用例，登录之后操作c是第三个用例，很明显三个用例都会走到登录。

如果登录都失败了，那后面2个用例就没测试必要了，直接跳过，并且标记为失败用例，这样可以节省用例时间。

用例设计

1.pytest里面用xfail标记用例为失败的用例，可以直接跳过。实现基本思路
把登录写为前置操作
对登录的账户和密码参数化，参数用canshu = [{“user”:”amdin”, “psw”:”12345”}]表示
多个用例放到一个Test_xx的class里
test_01，test_02， test_03全部调用fixture里面的login功能
test_01测试登录用例
test_02和test_03执行前用if判断登录的结果，登录失败就执行，pytest.xfail(“登录不成功, 标记为xfail”)
"""


import pytest

canshu = [{"user": "amdin", "psw": ""}]


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
正在操作登录，账号：amdin, 密码：
    用例1,登录结果：False
    用例2,登录结果：False
    用例3,登录结果：False
"""
