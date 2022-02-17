# !/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: yanghuizhi
# Time: 2022/2/17 11:30

import pytest
import allure
import json

# 模拟数据
url = "http://127.0.0.1"
method = "post"


class TestLogin(object):
    @allure.step("执行登录成功")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize(("username", "pwd"), [("zhangsan", "123321"), ("lisi", "32322")])
    def test_login_succ(self, username, pwd):
        route = "/api/login"
        data = {"username": username, "password": pwd}

        # 添加文本描述
        allure.attach(str(url + route), name="请求URL")  # 方式1
        allure.attach(json.dumps(data), "请求数据", allure.attachment_type.TEXT)  # 方式2

        # 添加图片描述
        allure.attach("./1.png", "图片", allure.attachment_type.PNG)

        assert 1

    @allure.severity(allure.severity_level.BLOCKER)
    def test_add_employee(self):
        data = {"name": "wangwu"}
        route = "/api/login"

        # 使用 with 添加测试步骤
        with allure.step("执行新增员工"):
            # 添加文本描述
            allure.attach(str(url + route), name="请求URL")
            allure.attach(json.dumps(data), name="请求数据")
        assert 0

    @allure.severity(allure.severity_level.NORMAL)
    def test_f1(self):
        assert 1

    @allure.severity(allure.severity_level.MINOR)
    def test_f2(self):
        assert 0

    @allure.severity(allure.severity_level.TRIVIAL)
    def test_f3(self):
        assert 1

    def test_f4(self):
        assert 1